# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 19:39:07 2018

@author: UO238186
"""

from __future__ import division   # forces floating point division 
from PIL import Image             # Python Imaging Library
import numpy as np                # Numerical Python 
import matplotlib.pyplot as plt   # Python plotting

# Create a chessboard, tiles being 250x250 pixels
tileSize = 250

# Prepare initial corner of four tiles, to later be repeated
initialSquare = np.zeros((tileSize*2,tileSize*2))
for i in range(0,tileSize*2):
    for j in range(0,tileSize*2):
        if ( (i < tileSize and j < tileSize) or (i >= tileSize and j >= tileSize) ):
            initialSquare[i,j] = 255;

# Extend initial corner with numpy.tile
chessboard = np.tile(initialSquare,(4,4))
image = Image.fromarray(chessboard.astype(np.uint8))
plt.imshow(image,cmap='gray',interpolation='none')
plt.show()

image.save('images/chessboard.jpg')