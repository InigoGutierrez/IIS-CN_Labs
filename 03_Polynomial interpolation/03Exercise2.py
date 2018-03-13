# -*- coding: utf-8 -*-
"""
Created on Tue Mar 06 19:17:34 2018

@author: UO238186
"""

import numpy as np
import matplotlib.pyplot as plt

def lagrange_fundamental(k,z,x):
    acc = 1.
    for i in range(len(x)):
        if i != k:
            acc *= (z-x[i])/(x[k]-x[i])
    return acc

def lagrange_polynomial(z,x,y):
    acc = 0.
    for i in range(len(x)):
        acc += y[i] * lagrange_fundamental(i,z,x)
    return acc

# First collection of nodes
x = np.array([2.,3.,4.,5.,6.])
y = np.array([0.,0.,1.,0.,0.])
z = np.linspace(min(x),max(x))
yy = lagrange_polynomial(z,x,y)

plt.plot(z,yy, label='function')
plt.plot(x,y, 'go', label='nodes')
plt.plot(x,x*0,'k-')
plt.legend()
plt.title('Exercise 2 - First nodes',fontsize=18)
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.show()

# Second collection of nodes
x = np.array([2.,3.,4.,5.,6.])
y = np.array([2.,6.,5.,5.,6.])
z = np.linspace(min(x),max(x))
yy = lagrange_polynomial(z,x,y)

plt.plot(z,yy, label='function')
plt.plot(x,y, 'ro', label='nodes')
plt.legend()
plt.title('Exercise 2 - Second nodes',fontsize=18)
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.show()

# First collection of nodes
x = np.array([0.,1.,2.,3.,4.,5.,6.])
y = np.array([3.,5.,6.,5.,4.,4.,5.])
z = np.linspace(min(x),max(x))
yy = lagrange_polynomial(z,x,y)

plt.plot(z,yy, label='function')
plt.plot(x,y, 'ro', label='nodes')
plt.legend()
plt.title('Exercise 2 - Third nodes',fontsize=18)
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.show()