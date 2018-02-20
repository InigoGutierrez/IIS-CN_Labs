# -*- coding: utf-8 -*-
import numpy as np

def de2bi_b(x):
    maxDigits = 23;
    acc = 0;
    result = []
    decimal = x - np.fix(x)
    if x < 0:
        decimal = -decimal
    while decimal != 0 and acc < maxDigits:
        decimal *= 2
        result.append(str(int(np.fix(decimal))))
        if decimal >= 1:
            decimal -= 1
        acc += 1
    return ''.join(result)

"""
x = -1.25
binary2 = de2bi_b(x)
print ''.join(binary2)  # if binary2 is stored as a strings' list
"""