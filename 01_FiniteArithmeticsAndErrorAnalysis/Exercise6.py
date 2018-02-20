# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12:35:06 2018

@author: UO238186
"""

import numpy as np
import math as math

x = 0.5
acc = 0
target = math.log1p(x)
spacing = np.spacing(target)
result = 0
while abs(target-result) != spacing:
    acc += 1
    if acc%2 == 1:
        result += (math.pow(x,acc)/acc)
    else:
        result -= (math.pow(x,acc)/acc)

print("Number of iterations: %d"%acc)
print("Error: %.16e"%(abs(target-result)))
print("Spacing: %.16e"%(spacing))