#!/usr/bin/python3

'''
This script is based on Newman's Example 8.2, which uses a
second-order Runge-Kutta method to solve:

    dx/dt = -x^3 + sin(t)

'''

from numpy import sin, arange
import matplotlib.pyplot as plt

def f(x,t):
    return - x**3 + sin(t)

a = 0.0
b = 10.0
Nvals = (10,20,50,100,200,1000)

plt.figure()

for N in Nvals:

    x = 0.0
    h = (b-a)/N
    tpoints = arange(a,b,h)
    xpoints = []
    
    for t in tpoints:

        xpoints.append(x)
        k1 = h*f(x,t)
        k2 = h*f(x + 0.5*k1, t + 0.5*h)
        x += k2

    plt.plot(tpoints,xpoints,label=str(N) + " steps")

plt.xlabel("t")
plt.ylabel("x(t)")
plt.title(r"dx/dt = -x^3 + sin(t)")
plt.legend()
plt.show()