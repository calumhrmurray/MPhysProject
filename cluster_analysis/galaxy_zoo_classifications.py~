# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 12:42:17 2016

@author: calum
"""

import numpy as np
import matplotlib.pyplot as plt

def plot_contour(x_contour,y_contour): 
    plt.figure()
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
    plt.contourf(xbins, ybins, vals.T, 20, zorder=10)
    plt.xlim([-23,-16])
    plt.ylim([0.1,3.4])
    plt.xlabel('M r,petro')
    plt.ylabel('(u-r)model')
    title_str = 'Observed bivariate distribution of the sample in rest-frame color vs. \
    absolute magnitude. Sample size '+str(len(x_contour))+' galaxies. Colour plot 150 bins, Contour 30 bins.'
    plt.title(title_str)
    plt.colorbar()
    
def db_plot(file_name):    
    array = np.load(file_name)
    
    x = []
    y = []
    e_x = []
    e_y = []
    s_x = []
    s_y = []
    # array x,y,redshift,dustval
    for i, row in enumerate(array):
            if array[i][2] > 0.004 and array[i][2] < 0.08:
               if array[i][1] > 0 and array[i][1] < 3.5:
                    if array[i][0] < -15.5 and array[i][0] > -23.5: 
                        x.append(array[i][0])
                        y.append(array[i][1])
                        # ellipticals
                        if array[i][3] > 0.75:
                            e_x.append(array[i][0])
                            e_y.append(array[i][1])
                        # spirals
                        elif array[i][4] > 0.75 or array[i][5] > 0.75:
                            s_x.append(array[i][0])
                            s_y.append(array[i][1])
                            
    plot_contour(x,y)
    plot_contour(e_x,e_y)
    plot_contour(s_x,s_y)

   
db_plot('/home/calum/Documents/MPhysProj/data/galaxy_zoo_classifications.npy')