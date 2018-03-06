# -*- coding: utf-8 -*-
"""
Created on Tue Mar 06 11:31:48 2018

@author: UO238186
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt

f = lambda x : x**3 - 75    # define the function

# prepare the graphic representation of the function
x = np.linspace(0,5,num=200)               # define the mesh
y = f(x)
OX = 0*x                            # define X axis

tol = 1.e-12
maxiter = 100

a = 3
b = 5
# find the zeroes with scipy
x0 = opt.bisect(f,a,b,xtol=tol,maxiter=maxiter)

# plot the zeroes and show the graph
plt.title('Exercise 8 - scipy',fontsize=18)
plt.plot(x,y,label='f function')
plt.plot(x,OX,'k-')
plt.plot([x0],[0], 'ro', label='zeroes')
plt.legend()
plt.show()

# find the zeroes with custom newton function
def bisection(f,a,b,tol = 1.e-12, maxiter = 200):
    n = 0
    sol = (a+b)/2.
    while n < maxiter and abs(b-sol) > tol:
        n += 1
        if f(a) * f(sol) < 0:
            b = sol
        else:
            a = sol
        sol = (a+b)/2.
    return (sol,n)

x0, n = bisection(f,a,b,tol,maxiter)

# plot the zeroes and show the graph
plt.title('Exercise 8 - custom function',fontsize=18)
plt.plot(x,y,label='f function')
plt.plot(x,OX,'k-')
plt.plot([x0],[0], 'ro', label='zeroes')
plt.legend()
plt.show()
