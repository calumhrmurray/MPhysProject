# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 10:32:38 2016

@author: calum
"""

import math
from astropy.cosmology import FlatLambdaCDM
import astropy.units as u
import numpy as np
import matplotlib.pyplot as plt
from astropy.cosmology import WMAP9 as cosmo1
from astropy.cosmology import Planck15 as cosmo2
from astropy.cosmology import LambdaCDM
from astropy.cosmology import wCDM 

def get_colour(u_model,r_model,Ku=0,Kr=0):
    Cur = ( u_model - Ku) - ( r_model - Kr )
    return Cur
    
def choose_cosmo_cm_diagram(cosmo):
    x = []
    y = []
    
    array = np.load('/home/calum/Documents/MPhysProj/mgs_sample/results_array.npy')
    
    print('Number of results:',len(array))
    print('Starting for loop...')
    
    for row in array:
        y_val = float(row[1]) - float(row[3])
        z = float(row[6])
        if y_val > 0 and y_val < 3.5:
        #    x.append( float(row[0]) - 5*( math.log(z*,10) - 1) )
            if z > 0.004 and z < 0.080:
                x_val = float(row[0])-5*(math.log(cosmo.luminosity_distance(z).to(u.pc).value/10 ,10))
                if x_val < -15.5 and x_val > -23.5:
                    x.append(x_val)
                    y.append(y_val)
                
    print('...finished for loop')
    
    print('Number of galaxies used:',len(x))
    
    # start with a rectangular figure
    fig = plt.figure() 
    fig.suptitle(cosmo)
    
    ax = plt.axes()
    
    # plot the data points
    ax.plot(x, y, ' ', markersize=0.5)
    
    # now let's overplot some contours. First we have to make a 2d
    # histogram of the point distribution.
    vals, xedges, yedges = np.histogram2d(x, y, bins=30)
    
    # Now we have the bin edges, but we want to find the bin centres to
    # plot the contour positions - they're half way between the edges:
    xbins = 0.5 * (xedges[:-1] + xedges[1:])
    ybins = 0.5 * (yedges[:-1] + yedges[1:])
    
    # now plot the contours
    ax.hist2d(x,y,bins=150)
    ax.contour(xbins, ybins, vals.T, 20, colors='k', zorder=10)
    ax.set_xlim([-23,-16])
    ax.set_ylim([0,3.5])
    ax.set_xlabel('M r,petro')
    ax.set_ylabel('(u-r)model')
    title_str = 'Observed bivariate distribution of the sample in rest-frame color vs. \
    absolute magnitude. Sample size '+str(len(x))+' galaxies. Colour plot 150 bins, Contour plot 30 bins.'
    ax.set_title(title_str)
    
    plt.show()
    
cosmo = FlatLambdaCDM(H0=70 * u.km / u.s / u.Mpc, Om0=0.3)
cosmo3 = wCDM(H0=70, Om0=0.3, Ode0=0.7, w0=-0.9)
cosmo4 = LambdaCDM(H0=70, Om0=0.3, Ode0=0.7)
cosmo5 = wCDM(H0=70, Om0=0, Ode0=0.7, w0=-0.9)

  
#choose_cosmo_cm_diagram(cosmo)
#choose_cosmo_cm_diagram(cosmo1)
choose_cosmo_cm_diagram(cosmo2)
#choose_cosmo_cm_diagram(cosmo3)
#choose_cosmo_cm_diagram(cosmo4)
#choose_cosmo_cm_diagram(cosmo5)
