# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 18:56:59 2018

@author: UO238186
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

#%%
def KernelRBF(X,Y,g):
    m = X.shape[0]
    n = Y.shape[0]
    K = np.zeros((m,n))
    
    for i in range(m):
        for j in range(n):
            dif = np.linalg.norm(X[i,:]-Y[j,:])
            K[i,j] = np.exp(-dif**2/g)
            
    return K 

#%%
folder = 'numbers1/'
data_train = np.loadtxt(folder + 'data_train1.txt')
labels_train = np.loadtxt(folder + 'labels_train1.txt')

data_test = np.loadtxt(folder + 'data_test1.txt')
labels_test = np.loadtxt(folder + 'labels_test1.txt')
#%%
C_list = [ 1., 10., 100., 1000.]
sigma_list = [1., 10., 100., 1000.]

number_classes = 10              # classes of digits

n = data_train.shape[0]          # number of rows (images) in training matrix
m = data_test.shape[0]           # number of rows (images) in testing matrix  
I = np.identity(n)
#%%
H = np.float_(data_train)/255   #the images are in [0,255]
H_te = np.float_(data_test)/255
#%%
Y = np.zeros((n, number_classes))
for i in range(0, n):
    Y[i, int(labels_train[i])] = 1
#%%
labels_te=np.zeros((m, number_classes))
for i in range(0, m):
    labels_te[i, int(labels_test[i])] = 1
#%%
bestPercent = 0
for C in C_list:
    for g in sigma_list:
        # Omega's 
        OmegaP = KernelRBF(H, H, g)  
        W = np.linalg.solve(I/C + OmegaP, Y)
        
        OmegaP_te = KernelRBF(H_te, H, g)
        YP_te = np.dot(OmegaP_te, W)
        
        # prediction
        predictedP_test = YP_te.argmax(axis=1)
        
        # success percentage
        percent = np.sum(predictedP_test == labels_test)/float(m)*100.
        print('C = '+str(C)+' sigma = '+str(g)+'\nSuccess rate = '+str(percent)+'%')
        if (percent > bestPercent):
            bestPercent = percent
            bestC = C
            bestG = g
            # confusion matrix
            mc = confusion_matrix(labels_test, predictedP_test)


print('Success rate = '+str(bestPercent)+'%, C = '+str(bestC)+', sigma = '+str(bestG))
# plot
plt.figure(figsize=(6,6))
ticks = range(number_classes)
plt.xticks(ticks)
plt.yticks(ticks)
plt.imshow(mc,cmap=plt.cm.Blues)
plt.colorbar(shrink=0.8)
w, h = mc.shape
for i in range(w):
    for j in range(h):
        plt.annotate(str(mc[i][j]), xy=(j, i), 
                    horizontalalignment='center',
                    verticalalignment='center')
plt.xlabel('Predicted label')
plt.ylabel('Actual label')
plt.title('Confusion matrix')
plt.show()