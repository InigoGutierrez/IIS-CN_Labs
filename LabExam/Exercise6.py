# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 18:18:13 2018

@author: UO238186
"""

import numpy as np
import matplotlib.pyplot as plt

def interpolate(xNodes,yNodes,x):
    y = np.zeros_like(x)
    nodePointer = 0
    prevX = xNodes[nodePointer]
    prevY = yNodes[nodePointer]
    nextX = xNodes[nodePointer+1]
    nextY = yNodes[nodePointer+1]
    for i in range(len(x)):
        if (x[i] > nextX): # change of interval
            nodePointer += 1
            prevX = xNodes[nodePointer]
            prevY = yNodes[nodePointer]
            nextX = xNodes[nodePointer+1]
            nextY = yNodes[nodePointer+1]
        y[i] = prevY + ((nextY-prevY)/(nextX-prevX)) * (x[i] - prevX)
    return y

def interpolateValue(xNodes,yNodes,x):
    nodePointer = 0
    prevX = xNodes[nodePointer]
    prevY = yNodes[nodePointer]
    nextX = xNodes[nodePointer+1]
    nextY = yNodes[nodePointer+1]
    while (x > nextX):
        nodePointer += 1
        prevX = xNodes[nodePointer]
        prevY = yNodes[nodePointer]
        nextX = xNodes[nodePointer+1]
        nextY = yNodes[nodePointer+1]
    return prevY + ((nextY-prevY)/(nextX-prevX)) * (x - prevX)

#%% First group of nodes
xNodes = [1,2,3,4,5]
yNodes = [2,5,4,4,5]
x = np.linspace(min(xNodes),max(xNodes),50)
y = interpolate(xNodes,yNodes,x)
z0 = 2.5134
yz = interpolateValue(xNodes,yNodes,z0)

plt.plot(x,y)
plt.plot(xNodes,yNodes, 'ro', label='nodes')
plt.plot(z0,yz, 'bo', label='yz')
plt.legend()
plt.title('Exercise 6 - First group of nodes',fontsize=18)
plt.show()
print("z = %.4f   yz = %.4f"%(z0,yz))

#%% Second group of nodes
xNodes = np.linspace(-10,10,10)
yNodes = xNodes*xNodes
x = np.linspace(min(xNodes),max(xNodes),50)
y = interpolate(xNodes,yNodes,x)
z0 = 2.5134
yz = interpolateValue(xNodes,yNodes,z0)

plt.plot(x,y)
plt.plot(xNodes,yNodes, 'ro', label='nodes')
plt.plot(z0,yz, 'bo', label='yz')
plt.legend()
plt.title('Exercise 6 - Second group of nodes',fontsize=18)
plt.show()
print("z = %.4f   yz = %.15f"%(z0,yz))