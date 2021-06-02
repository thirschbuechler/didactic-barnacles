# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 22:01:44 2020

@author: thirschbuechler
    
"""
import matplotlib.pyplot as plt
from matplotlib.patches import Arc
from scipy import interpolate
import numpy as np


#https://stackoverflow.com/questions/57555215/matplotlib-secondary-dual-axis-marking-with-circle-and-arrow-for-black-and
def ann_circlex(x, y, percx=33, orientation="r", scale=1):
    bw = np.max(x)-np.min(x)
    markerx = percx/100*(np.max(x) - np.min(x))  + np.min(x)
    
    markery=interpoly(xaxis=x, yaxis=y, xasked=markerx)

    x = markerx # $$ todo refactor belwo
    y = markery
    
    
    # Configure arc
    center_x = x            # x coordinate
    center_y = y            # y coordinate
    
    radius_2 = bw/5 * scale           # radius 2 >> for cicle: radius_2 = 2 x radius_1 $$$$$$$$$$$$actually diameter wtf
    radius_1 = radius_2/4         # radius 1 $$$$$$$$$$$$actually diameter wtf
    
    
    if orientation=="l":    # left, unusual
        angle = 180             # orientation
        sgn=-1
    else:
        angle=0
        sgn=1
        
    theta_1 = 70            # arc starts at this angle
    theta_2 = 290           # arc finishes at this angle
    arc = Arc([center_x, center_y],
              radius_1,
              radius_2,
              angle = angle,
              theta1 = theta_1,
              theta2=theta_2,
              capstyle = 'round',
              linestyle='-',
              lw=1,
              color = 'black')
    
    # Add arc
    ax.add_patch(arc)
    
    # Add arrow
    x1 = x + 0.1 *sgn            # x coordinate
    y1 = y + 0.2              # y coordinate    
    length_x = sgn*0.5 *scale     # length on the x axis (negative so the arrow points to the left)
    length_y = 0        # length on the y axis
    ax.arrow(x1,
             y1,
             length_x,
             length_y,
             head_width=0.1,
             head_length=0.05,
             fc='k',
             ec='k',
             linewidth = 0.6)
    
    
    #https://stackoverflow.com/questions/9850845/how-to-extract-points-from-a-graph
def interpoly(xaxis, yaxis, xasked):    #xasked can be array or value to find y vals
    #xnew = np.linspace(xaxis.min(),xaxis.max(),300)
    heights_smooth = interpolate.splrep(xaxis,yaxis) #Use splrep instead of spline
    

    #splev returns the value of your spline evaluated at the width values.    
    return interpolate.splev(xasked, heights_smooth)
    
    
             
        
        
#-#-# module test #-#-#
if __name__ == '__main__': # test if called as executable, not as library
    # Generate example graph
    fig = plt.figure(figsize=(5, 5))
    ax = fig.add_subplot(1, 1, 1)
    x,y = [1,2,3,4,5,6], [2,4,6,8,10,12]
    ax.plot(x,y)

    
    ann_circlex(x,y,50)
