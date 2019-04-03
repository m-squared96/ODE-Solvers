#!/usr/bin/python3
'''
This script is a solution to Exercise 8.5 of Newman and solves
the equations of motion for a nonlinear driven pendulum:

    d^2theta/dt^2 = -(g/l)sin(theta) + Ccos(theta)sin(Omega t)

By making the substitution 

    dtheta/dt = x

    dx/dt = -(g/l)sin(theta) + Ccos(theta)sin(Omega t)

and adhering to the following parameters:

g = 9.81 m/s^2
l = 10 cm
C = 2 s^-2
Omega = 5 s^-1

0 <= t <= 100

theta(0) = 0 degrees
x(0) = 0 degrees/s
'''

#TODO: Animate the motion of the pendulum

from numpy import sin,cos,arange,array,pi
import matplotlib.pyplot as plt

def f(r,Omega,t):
    
    g = 9.81
    l = 0.10
    C = 2

    theta = r[0]
    x = r[1]

    ftheta = x
    fx = -(g/l)*sin(deg2rad(theta)) + C*cos(deg2rad(theta))*sin(Omega*t)

    return array([ftheta,fx],float)

def deg2rad(angle):
    '''
    Accepts angle in degrees and returns angle in radians
    '''
    return float(angle*(pi/180))

plt.figure()
t0 = 0
T = 100
N = 1000
h = (T - t0)/N

tpoints = arange(t0,T,h)

for Omega in arange(1.0,1.5,0.1):

    thetapoints = []
    xpoints = []

    r = array([0,0],float)
    for t in tpoints:
        thetapoints.append(r[0])
        xpoints.append(r[1])
        
        k1 = h*f(r,Omega,t)
        k2 = h*f(r + 0.5*k1,Omega,t + 0.5*h)
        k3 = h*f(r + 0.5*k2,Omega,t + 0.5*h)
        k4 = h*f(r + k3,Omega,t + h)
        r += (k1 + 2*k2 + 2*k3 + k4)/6

    plt.plot(tpoints,thetapoints,label=r"$\Omega =$" + str(Omega))

plt.title("Driven Pendulum Solutions")
plt.xlabel(r"$t$")
plt.ylabel(r"$\theta$ (degrees)")
plt.legend()
plt.show()