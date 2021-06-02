# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 14:34:18 2020

@author: hirschbuechler
"""

stuff = ["Hello", "bye", "ello"]
matchers = ["ello"]
matching = [s for s in stuff if any(xs in s for xs in matchers)]
print(matching)