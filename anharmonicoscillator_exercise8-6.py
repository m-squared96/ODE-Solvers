#!/usr/bin/python3
'''
This script is a solution to Exercise 8.6 in Newman and
solves various harmonic and anharmonic oscillator equations
of motion:

a)      d^2x/dt^2 = -OMEGA^2 x
    for OMEGA = 1 and x(0) = 1, dx/dt(0) = 0. Then examine
    x(0) = 2.

b)      d^2x/dt^2 = -OMEGA^2 x^3
    with dx/dt(0) = 0 and x(0) = 1,2.

c)  Plot dx/dt vs x (aka "phase plot")

d)      d^2x/dt^2 - mu(1 - x^2)dx/dt + OMEGA^2 x = 0
    for:
        0 <= t <= 20
        OMEGA = 1
        mu = 1,2,4
        x(0) = 1
        dx/dt(0) = 0

        Produce phase plot also
'''

from numpy import array,arange
import matplotlib.pyplot as plt

NSTEPS = 100000
OMEGA = 1.0

def rk4(h,mu,tpoints,x0,y0,func):

    if func == fd:
        r = array([x0,y0],float)
        xpoints = []
        ypoints = []

        for t in tpoints:
            xpoints.append(r[0])
            ypoints.append(r[1])

            k1 = h*func(r,mu,t)
            k2 = h*func(r + 0.5*k1,mu,t + 0.5*h)
            k3 = h*func(r + 0.5*k2,mu,t + 0.5*h)
            k4 = h*func(r + k3,mu,t + h)
            r += (k1 + 2*k2 + 2*k3 + k4)/6

        xpoints = tuple(xpoints)
        ypoints = tuple(ypoints)

        return xpoints,ypoints

    elif func in (fa,fb):
        r = array([x0,y0],float)
        xpoints = []
        ypoints = []

        for t in tpoints:
            xpoints.append(r[0])
            ypoints.append(r[1])

            k1 = h*func(r,t)
            k2 = h*func(r + 0.5*k1,t + 0.5*h)
            k3 = h*func(r + 0.5*k2,t + 0.5*h)
            k4 = h*func(r + k3,t + h)
            r += (k1 + 2*k2 + 2*k3 + k4)/6

        xpoints = tuple(xpoints)
        ypoints = tuple(ypoints)

        return xpoints,ypoints

def fa(r,t):

    x = r[0]
    y = r[1]
    fx = y
    fy = -1*(OMEGA**2)*x

    return array([fx,fy],float)

def harmonic():

    print("Calculating harmonic oscillator solutions")

    t0 = 0
    T = 50
    h = (T - t0)/NSTEPS

    tpoints = arange(t0,T,h)
    
    x1, y1 = rk4(h,0,tpoints,1,0,fa)
    x2, y2 = rk4(h,0,tpoints,2,0,fa)          

    plt.figure()    
    plt.plot(tpoints,x1,label=r"$x(0)=1$")
    plt.plot(tpoints,x2,label=r"$x(0)=2$")
    plt.title(r"Harmonic Oscillator Solutions: $x(t)$")
    plt.xlabel(r"$t$")
    plt.ylabel(r"$x(t)$")
    plt.legend()

    plt.figure()
    plt.plot(x1,y1,label=r"$x(0)=1$")
    plt.plot(x2,y2,label=r"$x(0)=2$")
    plt.title("Harmonic Oscillator Phase Plot")
    plt.xlabel(r"$x$")
    plt.ylabel(r"$\dot{x}$")
    plt.legend()

    print("Completed harmonic oscillator calculations")

def fb(r,t):

    x = r[0]
    y = r[1]
    fx = y
    fy = -1*(OMEGA**2)*(x**3)

    return array([fx,fy],float)

def anharmonic():

    print("Calculating anharmonic oscillator solutions")

    t0 = 0
    T = 50
    h = (T - t0)/NSTEPS

    tpoints = arange(t0,T,h)
    
    x1, y1 = rk4(h,0,tpoints,1,0,fb)
    x2, y2 = rk4(h,0,tpoints,2,0,fb)          

    plt.figure()    
    plt.plot(tpoints,x1,label=r"$x(0)=1$")
    plt.plot(tpoints,x2,label=r"$x(0)=2$")
    plt.title(r"Anharmonic Oscillator Solutions: $x(t)$")
    plt.xlabel(r"$t$")
    plt.ylabel(r"$x(t)$")
    plt.legend()

    plt.figure()
    plt.plot(x1,y1,label=r"$x(0)=1$")
    plt.plot(x2,y2,label=r"$x(0)=2$")
    plt.title("Anharmonic Oscillator Phase Plot")
    plt.xlabel(r"$x$")
    plt.ylabel(r"$\dot{x}$")
    plt.legend()

    print("Completed anharmonic oscillator calculations")

def fd(r,mu,t):

    x = r[0]
    y = r[1]
    fx = y
    fy = mu*(1 - x**2)*y - (OMEGA**2)*x

    return array([fx,fy],float)

def vanderpol():

    print("Calculating Van der Pol oscillator solutions")

    t0 = 0
    T = 20
    h = (T - t0)/NSTEPS

    tpoints = arange(t0,T,h)

    x1, y1 = rk4(h,1,tpoints,1,0,fd)
    x2, y2 = rk4(h,2,tpoints,1,0,fd)
    x4, y4 = rk4(h,4,tpoints,1,0,fd)          

    plt.figure()    
    plt.plot(tpoints,x1,label=r"$\mu=1$")
    plt.plot(tpoints,x2,label=r"$\mu=2$")
    plt.plot(tpoints,x4,label=r"$\mu=4$")
    plt.title(r"Van der Pol Oscillator Solutions: $x(t)$")
    plt.xlabel(r"$t$")
    plt.ylabel(r"$x(t)$")
    plt.legend()

    plt.figure()
    plt.plot(x1,y1,label=r"$\mu=1$")
    plt.plot(x2,y2,label=r"$\mu=2$")
    plt.plot(x4,y4,label=r"$\mu=4$")
    plt.title("Van der Pol Oscillator Phase Plot")
    plt.xlabel(r"$x$")
    plt.ylabel(r"$\dot{x}$")
    plt.legend()

    print("Completed Van der Pol oscillator calculations")

harmonic()
anharmonic()
vanderpol()
plt.show()