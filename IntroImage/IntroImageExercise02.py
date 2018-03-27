# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 18:58:34 2018

@author: UO238186
"""

from __future__ import division   # forces floating point division 
from PIL import Image             # Python Imaging Library
import numpy as np                # Numerical Python 
import matplotlib.pyplot as plt   # Python plotting

def createCircularMask(maskXSize, maskYSize, centerX, centerY, circleRadius, maskValue):
    mask = np.ones((maskYSize,maskXSize))
    for i in range(maskYSize):
        for j in range(maskXSize):
            if ((i - centerY)**2 + (j - centerX)**2 > circleRadius**2):
                mask[i,j] = maskValue
    return mask
    

# Load image
folder = 'images/'
image = Image.open(folder + 'lena_gray_512.tif')
imageAsArray = np.asarray(image,dtype=np.double)

# Prepare masks
dimensions = len(imageAsArray)
centerX = dimensions/2
centerY = dimensions/2
circleRadius = 150
mask1 = createCircularMask(dimensions, dimensions, centerX, centerY, circleRadius, 0)
mask2 = createCircularMask(dimensions, dimensions, centerX, centerY, circleRadius, 0.5)

# Apply masks to image array
blackPixelsImage = Image.fromarray(np.multiply(imageAsArray,mask1).astype(np.uint8))
halfIntensityImage = Image.fromarray(np.multiply(imageAsArray,mask2).astype(np.uint8))

# Show results
plt.subplot(121) # 1 row, 2 columns, image 1
plt.imshow(blackPixelsImage,cmap='gray',interpolation='none')

plt.subplot(122) # 1 row, 2 columns, image 2
plt.imshow(halfIntensityImage,cmap='gray',interpolation='none')

plt.show()