# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 19:25:58 2018

@author: UO238186
"""

from __future__ import division   # forces floating point division 
from PIL import Image             # Python Imaging Library
import numpy as np                # Numerical Python 
import matplotlib.pyplot as plt   # Python plotting

def createDegradationMask(maskXSize, maskYSize):
    degradation = np.linspace(0,1,num=maskYSize)
    mask = np.zeros((maskYSize,maskXSize))
    for i in range(maskYSize):
        for j in range(maskXSize):
            mask[i,j] = degradation[i]
    return mask
    

# Load image
folder = 'images/'
image = Image.open(folder + 'lena_gray_512.tif')
imageAsArray = np.asarray(image,dtype=np.double)

# Prepare masks
dimensions = len(imageAsArray)
mask = createDegradationMask(dimensions, dimensions)

# Apply masks to image array
degradatedImage = Image.fromarray(np.multiply(imageAsArray,mask).astype(np.uint8))

# Show results
plt.subplot(121) # 1 row, 2 columns, image 1
plt.imshow(image,cmap='gray',interpolation='none')

plt.subplot(122) # 1 row, 2 columns, image 2
plt.imshow(degradatedImage,cmap='gray',interpolation='none')

plt.show()