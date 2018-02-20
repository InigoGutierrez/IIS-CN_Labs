# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 18:45:10 2018

@author: UO238186
"""

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

f = lambda x : x**3 - 2*x**2 + 1
tol = 10**-12
maxiter = 200
print("First zero: %.15f; Iterations: %d"%(bisection(f,-1,0,tol,maxiter)))
print("Second zero: %.15f; Iterations: %d"%(bisection(f,0.7,1.2,tol,maxiter)))
print("Third zero: %.15f; Iterations: %d"%(bisection(f,1.5,2,tol,maxiter)))