# -*- coding: utf-8 -*-
"""
Created on Tue Mar 06 18:30:48 2018

@author: UO238186
"""

import numpy as np
import matplotlib.pyplot as plt

def Vandermonde(x):
    size = len(x)
    A = np.zeros((size,size))
    for i in range(size):
        for j in range(size):
            A[i,j] = x[i]**j
    return A

# First collection of nodes
x = np.array([2.,3.,4.,5.,6.])
y = np.array([2.,6.,5.,5.,6.])
A = Vandermonde(x)
solutions = np.linalg.solve(A,y)
solutions = solutions[::-1] # flip

xx = np.linspace(min(x),max(x))
yy = np.polyval(solutions,xx)

plt.plot(xx,yy, label='function')
plt.plot(x,y, 'ro', label='nodes')
plt.legend()
plt.title('Exercise 1 - First nodes',fontsize=18)
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.show()

# Second collection of nodes
x = np.array([0.,1.,2.,3.,4.,5.,6.])
y = np.array([3.,5.,6.,5.,4.,4.,5.])
A = Vandermonde(x)
solutions = np.linalg.solve(A,y)
solutions = solutions[::-1] # flip

xx = np.linspace(min(x),max(x))
yy = np.polyval(solutions,xx)

plt.plot(xx,yy, label='function')
plt.plot(x,y, 'ro', label='nodes')
plt.legend()
plt.title('Exercise 1 - Second nodes',fontsize=18)
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.show()