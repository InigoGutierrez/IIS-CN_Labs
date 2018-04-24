# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 18:46:53 2018

@author: UO238186
"""

import numpy as np

def trapecio_simp(f,a,b):
    return ((b-a)/2.)*(f(a)+f(b))

def trapecio_comp(f,a,b,n):
    xNodes = np.linspace(a,b,n+1)
    acc = 0.
    for i in range(len(xNodes)-1):
        acc += trapecio_simp(f,xNodes[i],xNodes[i+1])
    return acc

#%% First data group
f = lambda x : np.exp(x)
a = 0
b = 3
n = 4
print("El valor aproximado para exp(x) es %.6f"%(trapecio_comp(f,a,b,n)))

#%% Second data group
f = lambda x : np.cos(x)
a = -np.pi/2
b = np.pi/2
n = 100
print("El valor aproximado para cos(x) es %.6f"%(trapecio_comp(f,a,b,n)))

#%% Third data group
f = lambda x : np.cosh(x)
a = -3
b = 3
n = 200
print("El valor aproximado para cosh(x) es %.6f"%(trapecio_comp(f,a,b,n)))