# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 19:36:54 2018

@author: UO238186
"""

import numpy as np
import matplotlib.pyplot as plt

def chebyshev(f,a,b,n):
    # Non Chebyshev way
    x = np.linspace(a,b,num=n)
    interpolatedNC = np.polyfit(x,np.polyval(f,x),n-1)
    
    # Chebyshev way
    for i in range(1, n+1):
        x[i] = np.cos((2*i-1)*np.pi/(2*n))
    interpolatedC = np.polyfit(x,np.polyval(f,x),n-1)
    
    return (interpolatedNC, interpolatedC)

a = -1
b = 1
f = lambda x : 1 / (1+25*x**2)
n = 11

# First collection of nodes
xx = np.linspace(-1,1)
yy = np.polyval(chebyshev[0](f,a,b,n),xx)
plt.plot(xx,yy, label='function')
#plt.plot(x,y, 'ro', label='nodes')
plt.legend()
plt.title('Exercise 3 - First nodes',fontsize=18)
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.show()