# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 18:13:10 2018

@author: UO238186
"""

from __future__ import division   # forces floating point division 
from PIL import Image             # Python Imaging Library
import numpy as np                # Numerical Python 
import matplotlib.pyplot as plt   # Python plotting

folder = 'images/'
#%%
I = Image.open(folder + 'lena.jpg')
#I.show()
I1=I.convert('L') # 'L' for gray scale mode

# Showing it as a numpy array
#plt.imshow(np.asarray(I1))
#plt.imshow(np.asarray(I1), cmap='gray')
#plt.show()
#%%
# Image class instance, I1, to float32 Numpy array, a
a = np.asarray(I1,dtype=np.float32)

# Manipulate the image
#    # Code
# Go back to rank 0 to 255
b = a.astype(np.uint8)
I3 = Image.fromarray(b)

I3.save(folder + 'test.jpg')
#%%
plt.imshow(a,cmap='gray')

Lena_eye=a[251:283,317:349]

plt.subplot(121) # 1 row, 2 columns, image 1
plt.imshow(a,cmap='gray',interpolation='none')
plt.title('Lena'),plt.axis('off') 

plt.subplot(122) # 1 row, 2 columns, image 2
plt.imshow(Lena_eye,cmap='gray',interpolation='none')
plt.title("Right Lena's eye"),plt.axis('off') 

plt.show()

Image.fromarray(Lena_eye.astype(np.uint8)).save(folder + 'LenaEye.jpg')
#%%
# Go back in rank
b = (b-np.min(b))/(np.max(b)-np.min(b))
b *= 255