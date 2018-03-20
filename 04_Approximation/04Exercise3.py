# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 19:38:44 2018

@author: UO238186
"""

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

e = 2
inte = lambda x: np.cos(x)

f = lambda x: x**2

a = -1
b = 1
I = quad(inte,a,b)[0] # quad returns a duple: integral and error bound