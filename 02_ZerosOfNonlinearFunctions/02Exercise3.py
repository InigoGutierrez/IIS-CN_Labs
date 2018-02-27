# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 18:20:07 2018

@author: UO238186
"""

def secant(f,x0,x1,tol = 1.e-12,maxiter = 200):
    n = 0
    sol = x0
    while n < maxiter and abs(x1-x0) > tol:
        n += 1
        sol = x1 - f(x1)*((x1-x0)/(f(x1)-f(x0)))
        x0 = x1
        x1 = sol
    return (sol, n)

f = lambda x : x**3 - 2*x**2 + 1
#df = lambda x : 3*x**2 - 4*x
tol = 1.e-12
maxiter = 200
print("First zero: %.15f; Iterations: %d"%(secant(f,-1,-0.5,tol,maxiter)))
print("Second zero: %.15f; Iterations: %d"%(secant(f,0.5,1.5,tol,maxiter)))
print("Third zero: %.15f; Iterations: %d"%(secant(f,1,1.8,tol,maxiter)))