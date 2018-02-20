# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 18:18:45 2018

@author: UO238186
"""

from __future__ import division
import scipy.optimize as op
f = lambda x: x**2-1.5
df = lambda x: 2*x
sol = op.newton(f,1.,df,tol=1.e-12)
print(sol)
#%%
a = 3/4
b = 3./4.
#%%
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1,2)               # define the mesh
f = lambda x : x**3 - 2*x**2 + 1    # define the function
y = f(x)
OX = 0*x                            # define X axis
plt.plot(x,y,label='f function')
plt.plot(x,OX,'k-')
plt.plot([0,1,2],[0.3,0.4,0.9], 'ro-', label='points')
plt.plot(1,0.8,'bo',label='isolated point')
plt.legend()
plt.title('Example',fontsize=18)
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.show()