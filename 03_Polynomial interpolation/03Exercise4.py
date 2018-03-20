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
    y = f(x)
    interpolatedNC = np.polyfit(x,y,n-1)
    
    # Chebyshev way
    for i in range(1, n+1):
        x[i-1] = np.cos((2*i-1)*np.pi/(2*n))
    y = f(x)
    interpolatedC = np.polyfit(x,y,n-1)
    
    return (interpolatedNC, interpolatedC)

a = -1
b = 1
f = lambda x : 1 / (1+25*x**2)
n = 11

spaceDots = 200

nodesX = np.linspace(a,b,num=n)
nodesY = f(nodesX)

# First collection of nodes
xx = np.linspace(a,b,num=spaceDots)
interpolatedNC, interpolatedC = chebyshev(f,a,b,n)
yy = np.polyval(interpolatedNC,xx)
plt.plot(xx,yy, 'r-', label='polynomial')
plt.plot(xx,f(xx), 'b-', label='function')
plt.plot(nodesX,nodesY, 'go', label='nodes')
plt.legend()
plt.title('Exercise 4 - First function - Equispaced nodes',fontsize=18)
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.show()

for i in range(1, n+1):
    nodesX[i-1] = np.cos((2*i-1)*np.pi/(2*n))
nodesY = f(nodesX)
yy = np.polyval(interpolatedC,xx)
plt.margins(0,0.4)
plt.plot(xx,yy, 'r-', label='polynomial')
plt.plot(xx,f(xx), 'b-', label='function')
plt.plot(nodesX,nodesY, 'go', label='nodes')
plt.legend()
plt.title('Exercise 4 - First function - Chebyshev nodes',fontsize=18)
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.show()


f = lambda x : np.exp(-20*x**2)
n = 15
nodesX = np.linspace(a,b,num=n)
nodesY = f(nodesX)

# Second collection of nodes
xx = np.linspace(a,b,num=spaceDots)
interpolatedNC, interpolatedC = chebyshev(f,a,b,n)
yy = np.polyval(interpolatedNC,xx)
plt.plot(xx,yy, 'r-', label='polynomial')
plt.plot(xx,f(xx), 'b-', label='function')
plt.plot(nodesX,nodesY, 'go', label='nodes')
plt.legend()
plt.title('Exercise 4 - Second function - Equispaced nodes',fontsize=18)
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.show()

for i in range(1, n+1):
    nodesX[i-1] = np.cos((2*i-1)*np.pi/(2*n))
nodesY = f(nodesX)
yy = np.polyval(interpolatedC,xx)
plt.margins(0,0.4)
plt.plot(xx,yy, 'r-', label='polynomial')
plt.plot(xx,f(xx), 'b-', label='function')
plt.plot(nodesX,nodesY, 'go', label='nodes')
plt.legend()
plt.title('Exercise 4 - Second function - Chebyshev nodes',fontsize=18)
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.show()