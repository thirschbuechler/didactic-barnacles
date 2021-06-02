#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 20:40:30 2020

@author: thomas
http://effbot.org/pyfaq/how-can-i-pass-optional-or-keyword-parameters-from-one-function-to-another.htm
"""

'''
def f(x, *args, **kwargs):
        kwargs['width']='14.3c'
        g(x, *args, **kwargs)
        
'''


#todo: x,y,myplot

#plt.myplot(x,y,"asdf",color='#00FF00')


'''

        if "color" in kwargs: # check for dict key
            if ""==kwargs["color"]:
                kwargs.remove("color") # remove any defaults
            else:
                pass # kwargs will be passed on fully
                
                
        if "outside" in kwargs:
            if kwargs["outside"]:
                yoff = 0 # would place it diagonally outside
                xoff = 0
            kwargs.pop("outside") # don't pass downstream matplotlib

'''
