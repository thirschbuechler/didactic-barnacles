#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 17:48:42 2020

@author: thomas
"""
import matplotlib.pyplot as plt
import numpy as np

from scipy.misc import electrocardiogram
from scipy.signal import find_peaks

      
y = electrocardiogram()[2000:4000]
print(np.shape(y))
#x, _ = find_peaks(y, distance=150)
#x_peaks, _ = find_peaks(y, distance=150)
x_peaks, _ = find_peaks(y, distance=150)

plt.plot(y) # ex
plt.stem(x_peaks,y[x_peaks]) # peaks, ex(peaks)