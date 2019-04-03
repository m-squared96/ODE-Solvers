#!/usr/bin/python3

'''
This script is based on Example 8.4 of Newman, and solves the equation

    dx/dt = 1/(x^2 + t^2)

from t=0 to t=inf with x(0) = 1. It does so by using the substitution

    u = 1/(1+t)

and then solving the equation

    dx/du = 1/(x^2(1 - u)^2 + u^2)

from u=0 to u=1, with x(u=0) = 1.
'''

from numpy import arange
from matplotlib.pyplot import xlabel,ylabel,xlim,plot,show,figure,title

def g(x,u):
    return 1/((x**2)*(1-u)**2 + u**2)

a = 0.0
b = 1.0
N = 100
h = (b-a)/N

upoints = arange(a,b,h)
tpoints = []
xpoints = []

x = 1.0
for u in upoints:
    tpoints.append(u/(1 - u))
    xpoints.append(x)

    k1 = h*g(x,u)
    k2 = h*g(x + 0.5*k1,u + 0.5*h)
    k3 = h*g(x + 0.5*k2,u + 0.5*h)
    k4 = h*g(x + k3,u + h)
    x += (k1 + 2*k2 + 2*k3 + k4)/6

figure()
title(r"Solution for $x(t)$")
plot(tpoints,xpoints)
xlabel(r"$t$")
ylabel(r"$x(t)$")
xlim(0,80)

figure()
title(r"Solution for $x(u)$")
plot(upoints,xpoints)
xlabel(r"$u$")
ylabel(r"$x(u)$")
xlim(0,1)

show()