# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 18:14:49 2018

@author: UO238186
"""

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
#%% Data
x = np.linspace(-1,1,5)
f = lambda x: np.cos(x)
y = f(x)
d = 2 # degree of the fitting polynomial
#%%
A = np.random.rand(4,2)
At = A.T
M = np.dot(At,A)
#%% First way
#M = np.zeros((3,3))
#for i in range(3):
#    for j in range(3):
#        M[i,j] = ...
#%% Second way
print(sum(x**4))
print(sum(x**2*y))