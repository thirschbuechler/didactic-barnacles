# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 15:20:28 2021

@author: https://stackoverflow.com/questions/34292076/pandas-bar-plot-how-to-annotate-grouped-horizontal-bar-charts
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns 

plt.close("all")


sns.set_style("white") #for aesthetic purpose only

# fake data
df = pd.DataFrame({'A': np.random.choice(['foo', 'bar'], 100),
                   'B': np.random.choice(['one', 'two', 'three'], 100),
                   'C': np.random.choice(['I1', 'I2', 'I3', 'I4'], 100),
                   'D': np.random.randint(-10,11,100),
                   'E': np.random.randn(100)})

p = pd.pivot_table(df, index=['A','B'], columns='C', values='D')
e = pd.pivot_table(df, index=['A','B'], columns='C', values='E')

ax = p.plot(kind='barh', xerr=e, width=0.85)

for r in ax.patches:
    w=r.get_width()
    #print(r.get_x()) # this always returns 0 - should have been "w" (experimental)
    print(w)
    if w < 0: # it it's a negative bar
        ax.text(0.25, # set label on the opposite side
                r.get_y() + r.get_height()/5., # y
                "{:" ">7.1f}%".format(w*100), # text
                bbox={"facecolor":"red", 
                      "alpha":0.5,
                      "pad":1},
                fontsize=10, family="monospace", zorder=10)
    else:
        ax.text(-1.5, # set label on the opposite side
                r.get_y() + r.get_height()/5., # y
                "{:" ">6.1f}%".format(w*100), 
                bbox={"facecolor":"green",
                      "alpha":0.5,
                      "pad":1},
                fontsize=10, family="monospace", zorder=10)
plt.tight_layout()