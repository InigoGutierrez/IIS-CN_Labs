# -*- coding: utf-8 -*-
"""
Created on Tue Feb 06 18:24:38 2018

@author: UO238186
"""

import numpy as np
x = 3.67
y = np.fix(x)
print 'x = ', x, 'y = ', y
#%% Example 1
a = 3
b = 2
if a==3:
    print 'hello'
elif b==2:
    print 'bye'
else:
    print 'none'
    
#%% Example 2
l = []
for i in range(5):
    l.append(i)
l.reverse()
print l

#%% Example 3
c = range(5)
d = np.arange(5)
e = c[:-1]
f = d[::-1]
print e
print f

#%%
k=0
while k < 7:
    k += 1
    print k

#%% function
def square(x):
    square = x*x
    return square
#------------
x = 4.56
print square(x)