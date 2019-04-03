#!/usr/bin/python3

'''
This script compares the Euler, RK2 & RK4 methods in
terms of the accuracy of the approximated function at
a given step count. The equation in question is:

    dx/dt = -x^3 + sin(t)

'''

from numpy import sin, arange
import matplotlib.pyplot as plt

def f(x,t):
    return - x**3 + sin(t)

a = 0.0
b = 10.0
Nvals = (10,50,100,500)

for N in Nvals:
    plt.figure()

    x_euler, x_rk2, x_rk4 = 0.0, 0.0, 0.0
    h = (b-a)/N
    tpoints = arange(a,b,h)
    
    eulerpoints = []
    rk2points = []
    rk4points = []
    
    for t in tpoints:

        eulerpoints.append(x_euler)
        x_euler += h*f(x_euler,t)

        rk2points.append(x_rk2)
        k1_rk2 = h*f(x_rk2,t)
        k2_rk2 = h*f(x_rk2 + 0.5*k1_rk2, t + 0.5*h)
        x_rk2 += k2_rk2

        rk4points.append(x_rk4)
        k1 = h*f(x_rk4,t)
        k2 = h*f(x_rk4 + 0.5*k1, t + 0.5*h)
        k3 = h*f(x_rk4 + 0.5*k2, t + 0.5*h) 
        k4 = h*f(x_rk4 + k3, t + h)      
        
        x_rk4 += (k1 + 2*k2 + 2*k3 + k4)/6

    plt.title("Number of steps: " + str(N))
    plt.plot(tpoints,eulerpoints,label="Euler")
    plt.plot(tpoints,rk2points,label="RK2")
    plt.plot(tpoints,rk4points,label="RK4")
    plt.legend()
    plt.xlabel(r"$t$")
    plt.ylabel(r"$x(t)$")

plt.show()