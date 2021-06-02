# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 10:31:25 2020

@author: hirschbuechler
"""
a = ["1", "2", "3", "4"]

#a.pop(1) next one is more user friendly
a.pop(a.index("2"))
print(a)