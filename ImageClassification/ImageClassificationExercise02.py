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
folder = 'characters/'
data = np.loadtxt(folder + 'data_char.txt')
labels = np.loadtxt(folder + 'labels_char.txt')

trainPercentage = 0.9

data_train = data[:len(data)*trainPercentage,:]
labels_train = labels[:len(labels)*trainPercentage]

data_test = data[len(data)*trainPercentage:,:]
labels_test = labels[len(labels)*trainPercentage:]
#%%
C = 1
sigma = 100

number_classes = 26             # classes of digits

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
# Omega's 
OmegaP = KernelRBF(H, H, sigma)  
W = np.linalg.solve(I/C + OmegaP, Y)

OmegaP_te = KernelRBF(H_te, H, sigma)
YP_te = np.dot(OmegaP_te, W)

# prediction
predictedP_test = YP_te.argmax(axis=1)

# success percentage
percent = np.sum(predictedP_test == labels_test)/float(m)*100.
print('C = '+str(C)+' sigma = '+str(sigma)+'\nSuccess rate = '+str(percent)+'%')

# confusion matrix
mc = confusion_matrix(labels_test, predictedP_test)

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