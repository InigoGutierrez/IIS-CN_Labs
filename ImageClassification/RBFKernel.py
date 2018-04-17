# -*- coding: utf-8 -*-
"""
RBF Kernel
"""
import numpy as np

def KernelRBF(X,Y,g):
    m = X.shape[0]
    n = Y.shape[0]
    K = np.zeros((m,n))
    
    for i in range(m):
        for j in range(n):
            dif = np.linalg.norm(X[i,:]-Y[j,:])
            K[i,j] = np.exp(-dif**2/g)
            
    return K 