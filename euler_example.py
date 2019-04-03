#!/usr/bin/python3

'''
This script is from Newman's 'Computational Physics' example 8.1.
Uses Euler's method to solve the equation:

    dx/dt = -x^3 + sin(t)

'''

from numpy import sin,arange
import matplotlib.pyplot as plt

def f(x,t):
    return -x**3 + sin(t)

a = 0.0         # Start of the interval
b = 10.0        # End of the interval
N = 10000       # Number of steps
h = (b-a)/N     # Step size
x = 0.0         # Initial condition

tpoints = arange(a,b,h)     # Time values
xpoints = []                # Initialising x(t)
for t in tpoints:
    xpoints.append(x)       # Appending inital condition x(0) = 0
    x += h*f(x,t)           # Euler's method: x(t + h) = x(t) + h*f(x,t)

plt.figure()
plt.plot(tpoints,xpoints)
plt.xlabel("t")
plt.ylabel("x(t)")
plt.show()