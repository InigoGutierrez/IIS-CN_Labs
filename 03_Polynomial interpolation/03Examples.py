# -*- coding: utf-8 -*-
"""
Created on Tue Mar 06 18:13:53 2018

@author: UO238186
"""

#Interpolation intro

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

#%% Data
x = np.array([2.,3.,4.,5.,6.])
y = np.array([2.,6.,5.,5.,6.])
n = len(x)
n = x.size

#%% Create a matrix
a = np.zeros((4,4))
b = np.ones((4,4))

#%% Fill the matrix
a[2,1] = 2
a[0,:] = [1,2,3,4]
b[:,2] = [2,3,4,5]
b[:,2] = b[:,2]*[2,3,4,5]
 
#%% fill v matrix
m = 10
v = np.zeros((m,m))
for i in range(m):
    for j in range(m):
        v[i,j] = i*100+j

#%% Solve a linear system Ax = b
A = np.random.rand(6,6)
b = np.random.rand(6)

x = np.linalg.solve(A,b)
x = x[::-1]

#%% Represent a polynomial
# P(x)= x**4 - 5x**3 - 1
p = [1,-5,0,0,-1]
xx = np.linspace(min(x),max(x))
yy = np.polyval(p,xx)
plt.plot(xx,yy)
plt.show()