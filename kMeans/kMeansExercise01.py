# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 18:15:45 2018

@author: UO238186
"""

import numpy as np
import matplotlib.pyplot as plt
#%%
def kMeans(X, nCentroids, dimensions, iterations): # only works for nCentroids = 3 and dimensions = 2
    
    # Initialization
    centroids = np.zeros((nCentroids,dimensions))
    
    for i in range(dimensions):
        centroids[:,i] = np.random.rand(nCentroids) # this rand creates an array with values [0,1) with dimensions its arguments
        m = min(X[:,i])
        M = max(X[:,i])
        centroids[:,i] = centroids[:,i]*(M-m)+m # move c values to [m,M] range
        
    plt.plot(X[:,0],X[:,1],'k.')
    plt.plot(centroids[:,0],centroids[:,1],'mo', label = 'centroids')
    plt.show()

    s1, s2 = X.shape
    
    # Iterations
    for iteration in range(1,iterations+1):
        
        #Select label for each point
        labels = np.zeros((s1)) # will store nearest centroid for each dot
        for i in range(s1):
            acc = 0
            for d in range(dimensions):
                acc += (centroids[0,d]-X[i,d])**2
            minD = np.sqrt(acc) # distance to centroid 0
            for c in range(1,nCentroids):
                acc = 0
                for d in range(dimensions):
                    acc += (centroids[c,d]-X[i,d])**2
                acc = np.sqrt(acc)
                if ( acc < minD ):
                    minD = acc
                    labels[i] = c
                
        plt.plot(X[labels==0,0],X[labels==0,1],'r.', label = 'cluster 1')
        plt.plot(X[labels==1,0],X[labels==1,1],'b.', label = 'cluster 2')
        plt.plot(X[labels==2,0],X[labels==2,1],'g.', label = 'cluster 3')
        plt.plot(centroids[:,0],centroids[:,1],'mo', label = 'centroids')
        plt.title('Assigned centroid to dots (it ' + str(iteration) + ')')
        plt.legend()
        plt.show()
        
        # Move centroid to center of its cluster
        clusterCounter = np.zeros((nCentroids))
        centroids = np.zeros((nCentroids,dimensions))
        for i in range(s1):
            clusterCounter[labels[i]] += 1
            for d in range(dimensions):
                centroids[labels[i],d] += X[i,d]
        for c in range(nCentroids):
            for d in range(dimensions):
                centroids[c,d] /= clusterCounter[c]
        
        
        plt.plot(X[labels==0,0],X[labels==0,1],'r.', label = 'cluster 1')
        plt.plot(X[labels==1,0],X[labels==1,1],'b.', label = 'cluster 2')
        plt.plot(X[labels==2,0],X[labels==2,1],'g.', label = 'cluster 3')
        plt.plot(centroids[:,0],centroids[:,1],'mo', label = 'centroids')
        plt.title('Moved centroids to center of cluster (it ' + str(iteration) + ')')
        plt.legend()
        plt.show()

#%%
np.random.seed(7)

x1 = np.random.standard_normal((100,2))*0.6+np.ones((100,2))
x2 = np.random.standard_normal((100,2))*0.5-np.ones((100,2))
x3 = np.random.standard_normal((100,2))*0.4-2*np.ones((100,2))+5
X = np.concatenate((x1,x2,x3),axis=0)

nCentroids = 3
dimensions = 2
kMeans(X,nCentroids,dimensions,7)