#!/usr/bin/python3
'''
This script is a solution to Exercise 8.4 of Newman and solves
the equations of motion for a nonlinear pendulum:

    d^2theta/dt^2 = -(g/l)sin(theta)

By making the substitution 

    dtheta/dt = omega

    domega/dt = -(g/l)sin(theta)

and adhering to the following parameters:

g = 9.81 m/s^2
l = 10 cm
theta(0) = 179 degrees
'''

#TODO: Animate the motion of the pendulum

from numpy import sin,arange,array,pi
import matplotlib.pyplot as plt

def f(r,t):
    
    g = 9.81
    l = 0.10

    theta = r[0]
    omega = r[1]

    ftheta = omega
    fomega = -(g/l)*sin(deg2rad(theta))

    return array([ftheta,fomega],float)

def deg2rad(angle):
    '''
    Accepts angle in degrees and returns angle in radians
    '''
    return float(angle*(pi/180))

t0 = 0
T = 60
N = 1000
h = (T - t0)/N

tpoints = arange(t0,T,h)
thetapoints = []
omegapoints = []

r = array([179,0],float)
for t in tpoints:
    thetapoints.append(r[0])
    omegapoints.append(r[1])
    
    k1 = h*f(r,t)
    k2 = h*f(r + 0.5*k1,t + 0.5*h)
    k3 = h*f(r + 0.5*k2,t + 0.5*h)
    k4 = h*f(r + k3,t + h)
    r += (k1 + 2*k2 + 2*k3 + k4)/6

plt.figure()
plt.plot(tpoints,thetapoints,label=r"$\theta (t)$")
plt.plot(tpoints,omegapoints,label=r"$\dot{\theta} (t)$")
plt.title("Nonlinear Pendulum Solutions")
plt.xlabel(r"$t$")
plt.legend()
plt.show()