# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 18:16:00 2018

@author: UO238186
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
#%%
data_train = np.loadtxt('data_train1.txt')
labels_train = np.loadtxt('labels_train1.txt')

data_test = np.loadtxt('data_test1.txt')
labels_test = np.loadtxt('labels_test1.txt')
#%%
plt.figure(figsize=(8,8))
for k in range(0, 100):
    plt.subplot(10, 10, k+1)
    image = data_train[k, ]
    image = image.reshape(28, 28)
    plt.imshow(image, cmap='gray')
    plt.axis('off')
plt.show()
#%%
C = 1                            # regularization
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
#Construct the model
Omega = np.dot(H, H.transpose())
W = np.linalg.solve(I/C + Omega, Y)
#Make predictions
Omega_te = np.dot( H_te, H.transpose())
Y_te = np.dot(Omega_te, W)

predicted_test  = Y_te.argmax(axis=1)

ttsp = np.sum(predicted_test == labels_test)/float(m)*100.
print('Testing success = %.1f%%' % ttsp)

#%%
mc = confusion_matrix(labels_test, predicted_test)

print('Confusion matrix')
print(mc)

plt.figure(figsize=(6,6))
ticks = range(10)
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
#%%
print('\nLabels predicted for testing samples')
for i in range(0,m):
    if i%10 == 0:
        print('\r')
        print(predicted_test[i]),
    else:
        print(predicted_test[i]),

print('\n')
print('Images corresponding to the above labels')
for k in range(0, 100):
    plt.subplot(10, 10, k+1)
    image = data_test[k, ]
    image = image.reshape(28, 28)
    plt.imshow(image, cmap=plt.cm.gray)
    plt.axis('off')
plt.show()