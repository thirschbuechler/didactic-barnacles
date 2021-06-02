# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 22:01:44 2020

@author: https://stackoverflow.com/questions/57555215/matplotlib-secondary-dual-axis-marking-with-circle-and-arrow-for-black-and
"""
import matplotlib.pyplot as plt
from matplotlib.patches import Arc

# Generate example graph
fig = plt.figure(figsize=(5, 5))
ax = fig.add_subplot(1, 1, 1)
ax.plot([1,2,3,4,5,6], [2,4,6,8,10,12])

# Configure arc
center_x = 2            # x coordinate
center_y = 3.8          # y coordinate
radius_1 = 0.25         # radius 1
radius_2 = 1            # radius 2 >> for cicle: radius_2 = 2 x radius_1
angle = 180             # orientation
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
x1 = 1.9            # x coordinate
y1 = 4              # y coordinate    
length_x = -0.5     # length on the x axis (negative so the arrow points to the left)
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