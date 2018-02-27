# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 18:34:06 2018

@author: UO238186
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt

f = lambda x : np.sin(x) - 0.1*x    # define the function
df = lambda x : np.cos(x) - 0.1

# prepare the graphic representation of the function
x = np.linspace(-1,20,num=200)               # define the mesh
y = f(x)
OX = 0*x                            # define X axis

tol = 1.e-12
maxiter = 100

# find the zeroes with scipy
x0 = opt.newton(f,0,df,tol=tol,maxiter=maxiter)
x1 = opt.newton(f,3,df,tol=tol,maxiter=maxiter)
x2 = opt.newton(f,6.5,df,tol=tol,maxiter=maxiter)
x3 = opt.newton(f,8,df,tol=tol,maxiter=maxiter)

# plot the zeroes and show the graph
plt.title('Exercise 6 - scipy',fontsize=18)
plt.plot(x,y,label='f function')
plt.plot(x,OX,'k-')
plt.plot([x0,x1,x2,x3],[0,0,0,0], 'ro', label='zeroes')
plt.legend()
plt.show()

# find the zeroes with custom newton function
def newton(f,df,x0,tol = 1.e-12,maxiter = 200):
    n = 0
    sol = x0
    while n < maxiter and abs(f(sol)) > tol:
        n += 1
        sol = sol - (f(sol)/df(sol))
    return (sol, n)

x0, n = newton(f,df,0,tol,maxiter)
x1, n = newton(f,df,3,tol,maxiter)
x2, n = newton(f,df,6.5,tol,maxiter)
x3, n = newton(f,df,8,tol,maxiter)

# plot the zeroes and show the graph
plt.title('Exercise 6 - custom function',fontsize=18)
plt.plot(x,y,label='f function')
plt.plot(x,OX,'k-')
plt.plot([x0,x1,x2,x3],[0,0,0,0], 'ro', label='zeroes')
plt.legend()
plt.show()
