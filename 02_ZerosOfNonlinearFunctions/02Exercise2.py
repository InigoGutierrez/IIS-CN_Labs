# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 19:24:01 2018

@author: UO238186
"""

def newton(f,df,x0,tol = 1.e-12,maxiter = 200):
    n = 0
    sol = x0
    while n < maxiter and f(sol) > tol:
        n += 1
        sol = sol - (f(sol)/df(sol))
    return (sol, n)

f = lambda x : x**3 - 2*x**2 + 1
df = lambda x : 3*x**2 - 4*x
tol = 1.e-12
maxiter = 200
print("First zero: %.15f; Iterations: %d"%(newton(f,df,-0.5,tol,maxiter)))
print("Second zero: %.15f; Iterations: %d"%(newton(f,df,1,tol,maxiter)))
print("Third zero: %.15f; Iterations: %d"%(newton(f,df,1.5,tol,maxiter)))