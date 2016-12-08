# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 10:09:00 2016

@author: calum
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


def plot_contour(x_contour,y_contour):            
   # start with a rectangular figure
    plt.figure()
    ax = plt.axes()
    
    # now let's overplot some contours. First we have to make a 2d
    # histogram of the point distribution.
    vals, xedges, yedges = np.histogram2d(x_contour, y_contour, bins=30)
    # for scaling
    tvals, txedges, tyedges = np.histogram2d(x_contour, y_contour, bins=150)
       
    # Now we have the bin edges, but we want to find the bin centres to
    # plot the contour positions - they're half way between the edges:
    xbins = 0.5 * (xedges[:-1] + xedges[1:])
    ybins = 0.5 * (yedges[:-1] + yedges[1:])
    
    # now plot the contours
    ax.contourf(xbins, ybins, vals.T, 20, zorder=10)
    ax.set_xlim([-23,-16])
    ax.set_ylim([0.1,3.4])
    #ax.set_ylim([0,3.5])
    ax.set_xlabel('M r,petro')
    ax.set_ylabel('(u-r)model')
    title_str = 'Observed bivariate distribution of the sample in rest-frame color vs. \
    absolute magnitude. Sample size '+str(len(x_contour))+' galaxies. Colour plot 150 bins, Contour 30 bins.'
    ax.set_title(title_str)    
    plt.draw()
    
def plot_hist(array):
    weights = np.ones_like(array)/len(array)
    n, bins, patches = plt.hist(array,bins=100,weights=weights)
    plt.close()
    return n, bins
    
    
def db_plot(file_name):    
    array = np.load(file_name)
    
    x = []
    y = []
    # array x,y,redshift,dustval
    for i, row in enumerate(array):
            if array[i][2] > 0.004 and array[i][2] < 0.08:
               if array[i][1] > 0 and array[i][1] < 3.5:
                    if array[i][0] < -15.5 and array[i][0] > -23.5: 
                        x.append(array[i][0])
                        y.append(array[i][1])
                        
    n,bins = plot_hist(y)
    plt.figure()                 
    plt.plot(n,bins[1:],label='Full sample')
    
    plot_contour(x,y)
    
db_plot('/home/calum/Documents/MPhysProj/vespa_searches/data/dust_extinction_dust2.npy')

