#!/usr/bin/python3
'''
This script is a solution to Exercise 8.2 of Newman and solves the
Lotka-Volterra equations:

    dx/dt = (alpha)x - (beta)xy, dy/dt = (gamma)xy - (delta)y

where x and y represent the populations of prey and predators in 1,000's
respectively (so they're approximately continuous to three decimal places).

Question asks for this system to be solved for the following parameters:

0 <= t <= 30

alpha = 1
beta = 0.5
gamma = 0.5
delta = 2

x(0) = y(0) = 2
'''

from numpy import arange,array
import matplotlib.pyplot as plt

def f(r,t):

    alpha = 1.0
    beta = 0.5
    gamma = 0.5
    delta = 2.0

    x = r[0]
    y = r[1]
    fx = alpha*x - beta*x*y
    fy = gamma*x*y - delta*y
    return array([fx,fy],float)

t0 = 0.0
T = 30.0
N = 1000
h = (T - t0)/N

tpoints = arange(t0,T,h)
xpoints = []
ypoints = []

r = array([2.0,2.0],float)
for t in tpoints:
    xpoints.append(r[0])
    ypoints.append(r[1])
    k1 = h*f(r,t)
    k2 = h*f(r + 0.5*k1,t + 0.5*h)
    k3 = h*f(r + 0.5*k2,t + 0.5*h)
    k4 = h*f(r + k3,t + h)
    r += (k1 + 2*k2 + 2*k3 + k4)/6

plt.figure()
plt.plot(tpoints,xpoints,label="Prey")
plt.plot(tpoints,ypoints,label="Predator")
plt.title("Predator-Prey populations over time")
plt.xlabel(r"$t$")
plt.ylabel("Population (1,000's)")
plt.legend()

plt.figure()
plt.plot(xpoints,ypoints)
plt.title("Predator-Prey populations as a function of each other")
plt.xlabel("Prey Population (1,000's)")
plt.ylabel("Predator Population (1,000's)")

plt.show()