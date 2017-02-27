# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 09:35:25 2016

@author: calum
"""

import math
from astropy.cosmology import FlatLambdaCDM
import astropy.units as u
import numpy as np
import matplotlib.pyplot as plt
import kcorrect 

# creates plot of contour with a scaled hist2d object behind it              
def plot_contour(x_contour,y_contour,x_colour,y_colour,x3,y3): 
    # start with a rectangular figure
    plt.figure()
    ax = plt.axes()
    plt.contour    
    # plot the data points
    ax.plot(x_contour, y_contour, ' ', markersize=0.5)
    
    # now let's overplot some contours. First we have to make a 2d
    # histogram of the point distribution.
    vals, xedges, yedges = np.histogram2d(x_contour, y_contour, bins=30)
    # for scaling
    tvals, txedges, tyedges = np.histogram2d(x_contour, y_contour, bins=150)
       
    # Now we have the bin edges, but we want to find the bin centres to
    # plot the contour positions - they're half way between the edges:
    xbins = 0.5 * (xedges[:-1] + xedges[1:])
    ybins = 0.5 * (yedges[:-1] + yedges[1:])
    
    
    rvals, rxedges, ryedges = np.histogram2d(x_colour, y_colour, bins=150)
    
    # Now we have the bin edges, but we want to find the bin centres to
    # plot the contour positions - they're half way between the edges:
    rxbins = 0.5 * (rxedges[:-1] + rxedges[1:])
    rybins = 0.5 * (ryedges[:-1] + ryedges[1:])   

    uvals= rvals#/(tvals+.0000001)
    
    # now plot the contours
    ax.plot(x_colour,y_colour,'g+')
    ax.plot(x3,y3,'b+')
    ax.contour(xbins, ybins, vals.T, 20, colors='k', zorder=10)
    ax.set_xlim([-23,-16])
    ax.set_ylim([0,3.5])
    ax.set_xlabel('M r,petro')
    ax.set_ylabel('(u-r)model')
    title_str = 'Observed bivariate distribution of the sample in rest-frame color vs. \
    absolute magnitude. Sample size '+str(len(x_colour))+' galaxies. Colour plot 150 bins, Contour 30 bins.'
    ax.set_title(title_str)    
    
# calculates k corrections using mag_u, mag_g ... and mag_u_err ,...
# arg z,mag_u,mag_g,mag_r,mag_i,mag_z,err_u,err_g,err_r,err_i,err_z
def get_kcorrections(row):
    maggies = np.array(pow(10,-0.4*row[1:6]))
    invar = pow(0.4*math.log(10)*maggies*np.array(row[6:12]),-2) 
    k_tuple = np.concatenate(([row[0]],maggies,invar))
    kcorrect_tuple = kcorrect.fit_coeffs(k_tuple)
    k_coeff = kcorrect.reconstruct_maggies(kcorrect_tuple)
    final_input = maggies/np.array(k_coeff[1:])
    return [-2.5*math.log(item,10) for item in final_input], k_coeff[0]


## setting things up    
#cosmo = FlatLambdaCDM(H0=70 * u.km / u.s / u.Mpc, Om0=0.3)
#kcorrect.load_templates()
#kcorrect.load_filters()
#
#galaxy_type = 'spirals'
#
#array = np.load('/home/calum/Documents/MPhysProj/data/galaxy_zoo_data/'+galaxy_type+'_array.npy')
#
#reduced_x = []
#reduced_y = []
#
#print('starting calculations')
#print(len(array))
#
#for row in array:
#    # kcorrect
#    kcorrection_array, z = get_kcorrections(row[1:])
#    # put above in a function probs 
#    y_val = float(row[2]) - kcorrection_array[1] - float(row[4]) + kcorrection_array[3]
#    if y_val > 0 and y_val < 3.5:
#        if z > 0.004 and z < 0.080:
#            x_val = float(row[0])-5*(math.log(cosmo.luminosity_distance(z).to(u.pc).value/10 ,10))
#            if x_val < -15.5 and x_val > -23.5: 
#                reduced_x.append(x_val)
#                reduced_y.append(y_val)
#                
#reduced_array = np.array([reduced_x,reduced_y])
#
#print('finished calculations')
#
#print(len(reduced_array[0]))
#
## vespa contour
#np.save('/home/calum/Documents/MPhysProj/data/galaxy_zoo_data/'+galaxy_type+'_array_contour.npy',reduced_array)                

# galaxy zoo contour
spiral_reduced_array = np.load('/home/calum/Documents/MPhysProj/data/galaxy_zoo_data/spirals_array_contour.npy')
elliptical_reduced_array = np.load('/home/calum/Documents/MPhysProj/data/galaxy_zoo_data/ellipticals_array_contour.npy')

# full contour                
array = np.load('/home/calum/Documents/MPhysProj/data/contour_plot.npy')
            
x = array[0]
y = array[1]

reduced_x = spiral_reduced_array[0]
reduced_y = spiral_reduced_array[1]

e_reduced_x = elliptical_reduced_array[0]
e_reduced_y = elliptical_reduced_array[1]

plot_contour(x,y,reduced_x,reduced_y,e_reduced_x,e_reduced_y)