#!/usr/bin/python3
'''
This script is based on Example 8.5 of Newman, and solves the system of
simultaneous first order ODEs from t=0 to t=10 for the case where omega=1
and with the initial condition that x(0) = y(0) = 1:

    dx/dt = xy - x, dy/dt = y - xy + (sin(omegat))^2
'''

from numpy import arange,array,sin
from matplotlib.pyplot import plot,xlabel,show,legend

def f(r,t):
    x = r[0]
    y = r[1]
    fx = x*y - x
    fy = y - x*y + sin(t)**2
    return array([fx,fy],float)

a = 0.0
b = 10.0
N = 1000
h = (b-a)/N

tpoints = arange(a,b,h)
xpoints = []
ypoints = []

r = array([1.0,1.0],float)
for t in tpoints:
    xpoints.append(r[0])
    ypoints.append(r[1])
    k1 = h*f(r,t)
    k2 = h*f(r + 0.5*k1,t + 0.5*h)
    k3 = h*f(r + 0.5*k2,t + 0.5*h)
    k4 = h*f(r + k3,t + h)
    r += (k1 + 2*k2 + 2*k3 + k4)/6

plot(tpoints,xpoints,label=r"$x(t)$")
plot(tpoints,ypoints,label=r"$y(t)$")
xlabel(r"$t$")
legend()
show()