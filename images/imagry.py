#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 11:23:13 2020

@author: thomas
"""

import matplotlib.pyplot as plt
from skimage import data, color
from skimage.transform import rescale, resize, downscale_local_mean

image = color.rgb2gray(data.astronaut())

image_rescaled = rescale(image, 0.25, anti_aliasing=False)
image_resized = resize(image, (image.shape[0] // 4, image.shape[1] // 4),
                       anti_aliasing=True)
image_downscaled = downscale_local_mean(image, (4, 3))

fs=.5,.5
fig, ax = plt.subplots(nrows=1, ncols=1, figsize=fs)


ax.imshow(image_resized, cmap='gray')
ax.set_title("Resized image (no aliasing)") # LPF - softened

plt.tight_layout()
plt.show()