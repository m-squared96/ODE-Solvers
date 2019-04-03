#!/usr/bin/python3
'''
This script is a solution to Exercise 8.3 of Newman and solves the
Lorenz equations:

    dx/dt = sigma(y - x),

    dy/dt = rx - y - xz,

    dz/dt = xy - bz

Question asks for this system to be solved for the following parameters:

0 <= t <= 50

sigma = 10
r = 28
b = 8/3

x(0) = 0
y(0) = 1
z(0) = 0

Plot y(t) and z against x
'''

from numpy import arange,array
import matplotlib.pyplot as plt

def f(vec,t):

    sigma = 10.0
    r = 28.0
    b = 8/3

    x = vec[0]
    y = vec[1]
    z = vec[2]

    fx = sigma*(y - x)
    fy = r*x - y - x*z
    fz = x*y - b*z

    return array([fx,fy,fz],float)

t0 = 0
T = 50
N = 100000
h = (T - t0)/N

tpoints = arange(t0,T,h)
xpoints = []
ypoints = []
zpoints = []

vec = array([0,1,0],float)
for t in tpoints:
    xpoints.append(vec[0])
    ypoints.append(vec[1])
    zpoints.append(vec[2])
    k1 = h*f(vec,t)
    k2 = h*f(vec + 0.5*k1,t + 0.5*h)
    k3 = h*f(vec + 0.5*k2,t + 0.5*h)
    k4 = h*f(vec + k3,t + h)
    vec += (k1 + 2*k2 + 2*k3 + k4)/6

plt.figure()
plt.plot(tpoints,xpoints,label=r"x(t)")
plt.plot(tpoints,ypoints,label=r"y(t)")
plt.plot(tpoints,zpoints,label=r"z(t)")
plt.title(r"Solution of $y(t)$")
plt.xlabel(r"$t$")
plt.ylabel(r"$y(t$")
plt.legend()

plt.figure()
plt.plot(xpoints,zpoints)
plt.title("The Lorenz Strange Attractor")
plt.xlabel(r"$x$")
plt.ylabel(r"$z$")

plt.show()