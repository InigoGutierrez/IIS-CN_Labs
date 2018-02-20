# -*- coding: utf-8 -*-
import numpy as np

def de2bi_a(x):
    sign = 0
    result = []
    quotient = np.fix(x)
    if quotient < 0:
        quotient = -quotient
        sign = 1
    while quotient > 0:
        result.append(str(int(quotient%2)))
        quotient = quotient // 2
    if result.count == 0:
        result.append(str(0))
    if sign == 1:
        result.append('-')
    result.reverse()
    return ''.join(result)

"""
x = 105.8125
binary1 = de2bi_a(x)
print ''.join(binary1)  # if binary1 is stored as a strings' list
"""