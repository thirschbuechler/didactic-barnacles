
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 18 21:26:53 2020

@author: thirschbuechler
"""
import re
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import EngFormatter
#from matplotlib.patches import Arc, Circle

from PIL import Image # pillow library
import cv2 # python-opencv library - linux:pip install opencv-python
#from skimage import idata, icolor
#from skimage.transform import rescale, resize, downscale_local_mean


# my modules
#-#-# module test #-#-#
testing=False # imports don't seem to traverse this before reaching EOF and complaining about undef_bool !?
if __name__ == '__main__': # test if called as executable, not as library
    import other_module as om
    testing=True
    #tester()#since this is no fct definition, can't call this, also py has no forward-declaration option
else:
    from submodule_dir import other_module as om
    #testing=False


## put actual submodule here ##
def tumbleweeds():
    """ well, there had to be something.. """
    om.external_fct("#")
    om.external_fct("I am useful!")
    om.external_fct("#")


## some testing fct could reside here ##
def tester():
    tumbleweeds()


#-#-# module test #-#-#
if testing:#call if selected, after defined, explanation see above
    tester()