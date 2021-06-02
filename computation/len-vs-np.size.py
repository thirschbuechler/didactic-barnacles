# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 13:57:31 2020

@author: hirschbuechler
"""

import numpy as np

x=["abc","bdd"]
print(len(x))#2
print(np.size(x))

x=x.pop(0)
print(len(x))#3
print(np.size(x))