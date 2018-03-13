# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 18:17:01 2018

@author: UO238186
"""

import numpy as np
import matplotlib.pyplot as plt

def div_dif(x,y):
    # Initialize matrix
    xCol = 0
    yCol = 1
    nRows = len(x)
    nCols = len(x)+1
    results = np.zeros((nRows,nCols))
    for i in range(nRows):
        results[i,xCol] = x[i]
        results[i,yCol] = y[i]
        
    # Iterate through columns calculating divided differences
    for col in range(2,nCols):
        for row in range(0,nRows-col+1):
            results[row,col] = (results[row,col-1]-results[row+1,col-1])/(results[row,xCol]-results[row+col-1,xCol])
    
    return results
        
def newton_polynomial(z,x,y):
    c = div_dif(x,y)[0][1:]
    solution = 0
    for i in range(len(c)):
        multiplier = c[i]
        for it in range(i):
            multiplier *= z-x[it]
        solution += multiplier
    return solution

# First collection of nodes
x = np.array([2.,3.,4.,5.,6.])
y = np.array([2.,6.,5.,5.,6.])
# print the divided differences matrix
print (div_dif(x,y))

z = np.linspace(min(x),max(x))
yy = newton_polynomial(z,x,y)
plt.plot(z,yy, label='function')
plt.plot(x,y, 'ro', label='nodes')
plt.legend()
plt.title('Exercise 3 - First nodes',fontsize=18)
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.show()

# Second collection of nodes
x = np.array([0.,1.,2.,3.,4.,5.,6.])
y = np.array([3.,5.,6.,5.,4.,4.,5.])
# print the divided differences matrix
print (div_dif(x,y))

z = np.linspace(min(x),max(x))
yy = newton_polynomial(z,x,y)
plt.plot(z,yy, label='function')
plt.plot(x,y, 'ro', label='nodes')
plt.legend()
plt.title('Exercise 3 - Second nodes',fontsize=18)
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.show()