# -*- coding: utf-8 -*-
"""
Created on Thu May  6 16:37:14 2021

@author: hirschbuechler
"""


import matplotlib.pyplot as plt
import numpy as np

plt.close("all")
fig, ax = plt.subplots(nrows=1, ncols=1)


data = np.array([[1,2,3,4,5,6], [1,1,1,5,1,1], [5,5,5,5,5,5]])
x_axis = np.arange(1E9,2E9,1E9/6)

# extent
#   - needed to set ticks and grid correctly (not shifted into centers)
#   - can also label
extent = (0, data.shape[1], data.shape[0], 0)
#print(extent)# with testdata: 0 1001 3 0
#extent = (np.min(x_axis), np.max(x_axis), magDBs.shape[0], 0)
#print(np.min(x_axis))
ax.imshow(data, aspect="auto", extent=extent, interpolation="none")#aspect makes it rect, interpol-none removes blurr
#ax.grid()#interpol off sufficient



# make x-axis
#np.arange(0,201,100)
#Out[80]: array([  0, 100, 200])
x_axiss = np.arange(np.min(x_axis)-1,np.max(x_axis)+1,(np.max(x_axis)-np.min(x_axis))/4)

#ax.set_xticks(x_axiss)
ax.set_xlabel(x_axis)