# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 19:29:55 2018

@author: UO238186
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt

f = lambda x : np.cosh(x) * np.cos(x) - 1    # define the function
df = lambda x : np.cos(x) * np.sinh(x) - np.cosh(x) * np.sin(x)

# prepare the graphic representation of the function
x = np.linspace(-1,20,num=200)               # define the mesh
y = f(x)
OX = 0*x                            # define X axis

tol = 1.e-12
maxiter = 100

# find the zeroes with scipy
x0 = opt.newton(f,17,tol=tol,maxiter=maxiter)

# plot the zeroes and show the graph
plt.title('Exercise 7 - scipy',fontsize=18)
plt.plot(x,y,label='f function')
plt.plot(x,OX,'k-')
plt.plot([x0],[0], 'ro', label='zeroes')
plt.legend()
plt.show()

# find the zeroes with custom newton function
def secant(f,x0,x1,tol = 1.e-12,maxiter = 200):
    n = 0
    sol = x0
    while n < maxiter and abs(x1-x0) > tol:
        n += 1
        sol = x1 - f(x1)*((x1-x0)/(f(x1)-f(x0)))
        x0 = x1
        x1 = sol
    return (sol, n)

x0, n = secant(f,17,20,tol,maxiter)

# plot the zeroes and show the graph
plt.title('Exercise 7 - custom function',fontsize=18)
plt.plot(x,y,label='f function')
plt.plot(x,OX,'k-')
plt.plot([x0],[0], 'ro', label='zeroes')
plt.legend()
plt.show()
