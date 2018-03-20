# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 18:14:49 2018

@author: UO238186
"""

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

a = -1
b = 1
n = 5
d = 2

x = np.linspace(a,b,n)
f = lambda x: np.cos(x)

y = f(x)
A = np.zeros((n,d+1))
for i in range(n):
   for j in range(d+1):
       A[i,j] = x[i]**j
At = A.T

coefficientMatrix = np.dot(At,A)
rightHandSideMatrix = np.dot(At,y)
solution = np.linalg.solve(coefficientMatrix,rightHandSideMatrix)

print("Coefficient matrix")
print(coefficientMatrix)
print()
print("Right hand side matrix")
print(rightHandSideMatrix)
print()
print("System solution")
print(solution)

xx = np.linspace(a,b)
yy = np.polyval(solution[::-1],xx)
plt.margins(0.1,0.4)
plt.plot(xx,yy, 'b-', label='approximating polynomial')
plt.plot(x,y, 'ro', label='nodes')
plt.legend()
plt.title('Exercise 1',fontsize=18)
plt.show()