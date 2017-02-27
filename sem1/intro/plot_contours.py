# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 19:09:36 2016

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
    ax.set_ylim([0,3.5])
    #ax.set_ylim([0,3.5])
    ax.set_xlabel('M r,petro')
    ax.set_ylabel('(u-r)model')
    ax.colorbar()
    title_str = 'Observed bivariate distribution of the sample in rest-frame color vs. \
    absolute magnitude. Sample size '+str(len(x_contour))+' galaxies. Colour plot 150 bins, Contour 30 bins.'
    ax.set_title(title_str)    
    plt.draw()
    
    
def scaled_plot(file_name_one, file_name_two):
    array_one = np.load(file_name_one)
    array_two = np.load(file_name_two)
    plot_scaled_contour(array_one[0],array_one[1],array_two[0],array_two[1])
    
scaled_plot('/home/calum/Documents/MPhysProj/data/contour_plot.npy',
      '/home/calum/Documents/MPhysProj/data/more_colours_redshift_008_01.npy') 
scaled_plot('/home/calum/Documents/MPhysProj/data/vespa_data/vespa_smf_0.1_contour.npy',
      '/home/calum/Documents/MPhysProj/data/vespa_data/vespa_smf_0.8_contour.npy') 

# redshift stuff
#scaled_plot('/home/calum/Documents/MPhysProj/data/more_colours_redshift_0004_008.npy',
#      '/home/calum/Documents/MPhysProj/data/more_colours_redshift_0004_008.npy')    
#scaled_plot('/home/calum/Documents/MPhysProj/data/more_colours_redshift_0004_008.npy',
#      '/home/calum/Documents/MPhysProj/data/more_colours_redshift_008_01.npy')
#scaled_plot('/home/calum/Documents/MPhysProj/data/more_colours_redshift_0004_008.npy',
#      '/home/calum/Documents/MPhysProj/data/more_colours_redshift_01_02.npy')
#scaled_plot('/home/calum/Documents/MPhysProj/data/more_colours_redshift_0004_008.npy',
#      '/home/calum/Documents/MPhysProj/data/more_colours_redshift_02_04.npy')
#scaled_plot('/home/calum/Documents/MPhysProj/data/more_colours_redshift_0004_008.npy',
#      '/home/calum/Documents/MPhysProj/data/more_colours_redshift_04_07.npy')
#scaled_plot('/home/calum/Documents/MPhysProj/data/more_colours_redshift_0004_008.npy',
#      '/home/calum/Documents/MPhysProj/data/more_colours_redshift_07_1.npy')   
#scaled_plot('/home/calum/Documents/MPhysProj/data/more_colours_redshift_0004_008.npy',
#      '/home/calum/Documents/MPhysProj/data/more_colours_redshift_1_14.npy')      
