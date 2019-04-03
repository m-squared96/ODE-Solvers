#!/usr/bin/python3
'''
This script is a solution for Exercise 8.8 of Newman and
solves the system of simultaneous 2nd order ODEs:

    d^2x/dt^2 = -GM(x/(r^2 sqrt(r^2 + L^2/4)))
    
    d^2y/dt^2 = -GM(y/(r^2 sqrt(r^2 + L^2/4)))

By making the substitutions

    dx/dt = p

    dy/dt = q

with the parameters:

    0 <= t <= 10
    M = 10
    G = 1
    L = 2

    x(0) = 1
    y(0) = 0
    p(0) = 0
    q(0) = 1
'''

from numpy import array,arange,sqrt
import matplotlib.pyplot as plt

def f(vec,t):

    G = 1
    M = 10
    L = 2

    x = vec[0]
    y = vec[1]
    p = vec[2]
    q = vec[3]

    r = sqrt(x**2 + y**2)

    xdot = p
    ydot = q
    pdot = (-1*G*M*x)/((r**2)*sqrt(r**2 + 0.25*L**2))
    qdot = (-1*G*M*y)/((r**2)*sqrt(r**2 + 0.25*L**2))

    return array([xdot,ydot,pdot,qdot],float)

t0 = 0
T = 10
N = 1000
h = (T - t0)/N

tpoints = arange(t0,T,h)
xpoints = []
ypoints = []
ppoints = []
qpoints = []

r = array([1,0,0,1],float)
for t in tpoints:

    for seq,ind in zip((xpoints,ypoints,ppoints,qpoints),(0,1,2,3)):

        seq.append(r[int(ind)])

    k1 = h*f(r,t)
    k2 = h*f(r + 0.5*k1,t + 0.5*h)
    k3 = h*f(r + 0.5*k2,t + 0.5*h)
    k4 = h*f(r + k3,t + h)
    r += (k1 + 2*k2 + 2*k3 + k4)/6

plt.plot(xpoints,ypoints)
plt.show()