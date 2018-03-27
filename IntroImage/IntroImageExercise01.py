# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 18:46:12 2018

@author: UO238186
"""

from __future__ import division   # forces floating point division 
from PIL import Image             # Python Imaging Library
import numpy as np                # Numerical Python 
import matplotlib.pyplot as plt   # Python plotting


def cropImage(image, x0, x1, y0, y1):
    array = np.asarray(image,dtype=np.float32)
    croppedArray = array[y0:y1, x0:x1]
    croppedArrayInts = croppedArray.astype(np.uint8)
    resultImage = Image.fromarray(croppedArrayInts)
    return (croppedArray, resultImage)

folder = 'images/'
image = Image.open(folder + 'cameraman.tif')
x0 = 180
x1 = 280
y0 = 65
y1 = 165
croppedImage = cropImage(image,x0,x1,y0,y1)[0]

plt.subplot(121) # 1 row, 2 columns, image 1
plt.imshow(image,cmap='gray',interpolation='none')
plt.title('Cameraman')

plt.subplot(122) # 1 row, 2 columns, image 2
plt.imshow(croppedImage,cmap='gray',interpolation='none')
plt.title("Cameramans head") 

plt.show()