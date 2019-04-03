#!/usr/bin/python3
'''
This script is a solution to Exercise 8.7 of Newman and models the
displacement of a cannonball by solving the equations:

    d^2x/dt^2 = -(pi R^2 rho C/2m) dx/dt sqrt(dx/dt^2 + dy/dx^2)

    d^2y/dt^2 = -g -(pi R^2 rho C/2m) dy/dt sqrt(dx/dt^2 + dy/dx^2)

By making the substitution

    lambda = dx/dt
    omega = dy/dt

with    x(0) = 0
        y(0) = 0
        lambda(0) = 50sqrt(3)
        omega(0) = 50

Plot the trajectory (x vs y) and examine the effect of the mass on the
distance travelled.
'''

#TODO: Extract and plot m vs xmax data

from numpy import sqrt,pi,arange,array,cos,sin
import matplotlib.pyplot as plt

def f(r,m,t):

    g = -9.81
    R = 0.08
    rho = 1.22
    C = 0.47

    x = r[0]
    y = r[1]
    lambda_var = r[2]
    omega = r[3]

    #for var,val in zip(("x","y","lambda_var","omega","m"),(x,y,lambda_var,omega,m)):
    #    print(var + ": " + str(val))

    xdot = lambda_var
    ydot = omega
    lambdadot = -1*((pi*(R**2)*rho*C/(2*m)))*lambda_var*sqrt(lambda_var**2 + omega**2)
    omegadot = g + -1*((pi*(R**2)*rho*C/(2*m)))*omega*sqrt(lambda_var**2 + omega**2)

    return array([xdot,ydot,lambdadot,omegadot],float)

def deg2rad(angle):
    '''
    Accepts angle in degrees and returns angle in radians
    '''
    return float(angle*(pi/180))

theta0 = 30 #Initial angle in degrees wrt horizontal
v0 = 100 #Magnitude of initial velocity in m/s
lambda0 = v0*cos(deg2rad(theta0)) #Initial velocity in x-direction
omega0 = v0*sin(deg2rad(theta0)) #Initial velocity in y-direction

masslist = arange(1.0,11.0,2.0)

t0 = 0
T = 15
N = 1000
h = (T - t0)/N

tpoints = arange(t0,T,h)

plt.figure()
for m in masslist:

    print("Calculating for m = " + str(m) + " kg")

    xpoints = []
    ypoints = []
    lambdapoints = []
    omegapoints = []

    r = array([0,0,lambda0,omega0],float)

    for t in tpoints:

        xpoints.append(r[0])
        ypoints.append(r[1])
        lambdapoints.append(r[2])
        omegapoints.append(r[3])

        k1 = h*f(r,m,t)
        k2 = h*f(r + 0.5*k1,m,t + 0.5*h)
        k3 = h*f(r + 0.5*k2,m,t + 0.5*h)
        k4 = h*f(r + k3,m,t + h)
        r += (k1 + 2*k2 + 2*k3 + k4)/6

    plt.plot(xpoints,ypoints,label="m = " + str(m) + " kg")

print("Done")

plt.title("Cannonball Trajectory")
plt.xlabel(r"$x(t)$ (m)")
plt.ylabel(r"$y(t)$ (m)")
plt.xlim(left=0)
plt.ylim(bottom=0)
plt.legend()
plt.show()