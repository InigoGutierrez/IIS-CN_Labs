# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 19:09:04 2018

@author: UO238186
"""

import sys

result = 0
for exp in range(-52, 1):
    result += 2**exp
result *= 2**1023
print('Result: %.16e; Max value: %.16e; Equal: %s'%(result,
                                                    sys.float_info.max,
                                                    result == sys.float_info.max))