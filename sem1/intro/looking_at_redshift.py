# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 17:42:48 2016

@author: calum
"""

import math
from astropy.cosmology import FlatLambdaCDM
import astropy.units as u
import numpy as np
import kcorrect 

def looking_at_redshift(z_low,z_high,name):
    # setting things up    
    cosmo = FlatLambdaCDM(H0=70 * u.km / u.s / u.Mpc, Om0=0.3)
    kcorrect.load_templates()
    kcorrect.load_filters()
    
    # form of input for fit_coeff
    # redshift umaggies gmaggies rmaggies imaggies zmaggies uinvvar ginvvar rinvvar iinvvar zinvvar
    # output: redshift u_rec g_rec r_rec i_rec z_rec
           
    x = []
    y = []
    
    array = np.load('/home/calum/Documents/MPhysProj/mgs_sample/mgs_kcorrect_array.npy')
    
    print('Number of results:',len(array))
    print('Starting for loop...')
    
    # need to sort out the coefficents so they're in units of maggies!
    #Note that the conversion to the inverse variances from the maggies and the magnitude errors is (0.4 ln(10) × maggies × magerr)-2
    # maggies are simply related to magnitudes by 10−0.4m
    for row in array:
        # kcorrect
        maggies = np.array(pow(10,-0.4*row[2:7]))
        invar = pow(0.4*math.log(10)*maggies*np.array(row[7:]),-2) 
        k_tuple = np.concatenate(([row[1]],maggies,invar))
        kcorrect_tuple = kcorrect.fit_coeffs(k_tuple)
        k_coeff = kcorrect.reconstruct_maggies(kcorrect_tuple)
        final_input = maggies/np.array(k_coeff[1:])
        kcorrection_array = [-2.5*math.log(item,10) for item in final_input]
        # put above in a function probs 
        y_val = float(row[2]) - kcorrection_array[1] - float(row[4]) + kcorrection_array[3]
        z = k_coeff[0]
        if y_val > 0 and y_val < 6.5:
            if z > z_low and z < z_high:
                x_val = float(row[0])-5*(math.log(cosmo.luminosity_distance(z).to(u.pc).value/10 ,10))
                if x_val < -15.5 and x_val > -23.5: 
                    x.append(x_val)
                    y.append(y_val)
                    
    contour_plot_array = np.array([x,y])
    print('Length of output:',len(x))
                    
    np.save('/home/calum/Documents/MPhysProj/data/'+name+'.npy',contour_plot_array)
    print('Finished:',name)
    
looking_at_redshift(0.,20.,'all_colours_all_redshift')    
#looking_at_redshift(0.080,0.1,'more_colours_redshift_008_01')
#looking_at_redshift(0.1,0.2,'more_colours_redshift_01_02')
#looking_at_redshift(0.2,0.4,'more_colours_redshift_02_04')
#looking_at_redshift(0.4,0.7,'more_colours_redshift_04_07')
#looking_at_redshift(0.7,1.0,'more_colours_redshift_07_1')
#looking_at_redshift(1.0,1.4,'more_colours_redshift_1_14')