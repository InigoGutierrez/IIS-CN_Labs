# -*- coding: utf-8 -*-

import Exercise1 as ex1
import Exercise2 as ex2

arrow = '--->'
bias = 127
expSize = 8
mantSize = 23

values = [105.8125, 120.875, 7.1, -1.41]

for value in values:
    integer = ex1.de2bi_a(value)
    if value < 0:
        integer = integer[1:] # remove - symbol
    decimal = ex2.de2bi_b(value)
    sign = 0
    if value < 0:
        sign = 1
    exponent = 0
    mantissa = integer + decimal
    # if integer == 0, mantissa searchs first one to the right; if not, mantissa already has first one as first char (except -)
    if value > -1 and value < 1:
        while mantissa[:1] == '0': # find first 1
            exponent -= 1
            mantissa = mantissa[1:]
    else:
        exponent = len(integer)-1
    mantissa = mantissa[1:] # remove implicit 1
    # convert exponent to binary with bias
    exponentBinary = ex1.de2bi_a(exponent+bias)
    while len(exponentBinary) < expSize:
        exponentBinary = '0' + exponentBinary
    while len(mantissa) < mantSize:
        mantissa = mantissa + '0'
    while len(mantissa) > mantSize:
        mantissa = mantissa[:len(mantissa)-1]
            
    print('%f %s %s.%s'%(value, arrow, integer, decimal))
    print('[Sign]: %d [Exponent]: %s [Mantissa]: %s\n'%(sign, exponentBinary, mantissa))