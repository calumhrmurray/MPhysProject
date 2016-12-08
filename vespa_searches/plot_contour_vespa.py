# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 11:34:36 2016

@author: calum
"""

import numpy as np
import matplotlib.pyplot as plt
              
# creates plot of contour with a scaled hist2d object behind it              
def plot_scaled_contour(x_contour,y_contour,x_colour,y_colour):            
   # start with a rectangular figure
    plt.figure()
    ax = plt.axes()
    
    tvals, txedges, tyedges = np.histogram2d(x_colour, y_colour, bins=150)
    vals, xedges, yedges = np.histogram2d(x_contour, y_contour, bins=150)
    lvals, lxedges, lyedges = np.histogram2d(x_contour, y_contour, bins=30)

    
    # scale histogram
    rvals = tvals/(vals+pow(1,-10000000))
    
    xbins = 0.5 * (xedges[:-1] + xedges[1:])
    ybins = 0.5 * (yedges[:-1] + yedges[1:])
    
    lxbins = 0.5 * (lxedges[:-1] + lxedges[1:])
    lybins = 0.5 * (lyedges[:-1] + lyedges[1:])    
    
    ax.contourf(xbins, ybins, rvals.T, 20, zorder=10)  
    ax.contour(lxbins, lybins, lvals.T, 20, colors='w', zorder=10)
    ax.set_xlim([-23,-16])
    ax.set_xlabel('M r,petro')
    ax.set_ylabel('(u-r)model')
    title_str = 'Observed bivariate distribution of the sample in rest-frame color vs. \
    absolute magnitude. Sample size '+str(len(x_colour))+' galaxies. Colour plot 150 bins, Contour 30 bins.'
    ax.set_title(title_str)    
    plt.draw()
    
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
    
    
def db_plot(file_name):    
    array = np.load(file_name)
    
    x = []
    y = []
    rx = []
    ry = []
    lx = []
    ly = []
    d = []
    # array x,y,redshift,dustval
    for i, row in enumerate(array):
            if array[i][2] > 0.004 and array[i][2] < 0.08:
               if array[i][1] > 0 and array[i][1] < 3.5:
                    if array[i][0] < -15.5 and array[i][0] > -23.5: 
                        x.append(array[i][0])
                        y.append(array[i][1])
                        d.append(array[i][3])
                        if array[i][3] > 0.8:
                            rx.append(array[i][0])
                            ry.append(array[i][1])
                        if array[i][3] < 0.8:
                            lx.append(array[i][0])
                            ly.append(array[i][1])
    plt.close()
    plt.figure()                    
    plt.hist(d, bins= 100)
            
    plot_contour(x,y)
    plot_contour(rx,ry)
    plot_contour(lx,ly)

   
db_plot('/home/calum/Documents/MPhysProj/vespa_searches/data/dust_extinction_dust2.npy')
        
    

