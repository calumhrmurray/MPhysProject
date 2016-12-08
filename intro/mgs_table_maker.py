# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 09:42:42 2016

@author: calum
"""

import math
from astropy.cosmology import FlatLambdaCDM
import astropy.units as u
import numpy as np
import kcorrect 

def get_colour(u_model,r_model,Ku=0,Kr=0):
    Cur = ( u_model - Ku) - ( r_model - Kr )
    return Cur

# setting things up    
cosmo = FlatLambdaCDM(H0=70 * u.km / u.s / u.Mpc, Om0=0.3)
kcorrect.load_templates()
kcorrect.load_filters()

# form of input for fit_coeff
# redshift umaggies gmaggies rmaggies imaggies zmaggies uinvvar ginvvar rinvvar iinvvar zinvvar
# output: redshift u_rec g_rec r_rec i_rec z_rec
specObj = []    
x = []
y = []
redshift_array = []

array = np.load('/home/calum/Documents/MPhysProj/mgs_sample/mgs_array.npy')

print('Number of results:',len(array))
print('Starting for loop...')

# need to sort out the coefficents so they're in units of maggies!
#Note that the conversion to the inverse variances from the maggies and the magnitude errors is (0.4 ln(10) × maggies × magerr)-2
# maggies are simply related to magnitudes by 10−0.4m
for row in array:
    # kcorrect
    maggies = np.array(pow(10,-0.4*row[2:7]))
    invar = pow(0.4*math.log(10)*maggies*np.array(row[7:12]),-2) 
    k_tuple = np.concatenate(([row[1]],maggies,invar))
    kcorrect_tuple = kcorrect.fit_coeffs(k_tuple)
    k_coeff = kcorrect.reconstruct_maggies(kcorrect_tuple)
    final_input = maggies/np.array(k_coeff[1:])
    kcorrection_array = [-2.5*math.log(item,10) for item in final_input]
    # put above in a function probs 
    y_val = float(row[2]) - kcorrection_array[1] - float(row[4]) + kcorrection_array[3]
    z = k_coeff[0]
    if z > 0:
        if np.isnan(y_val):
            print('do not worry, everything is fine now')
        else:
            x_val = float(row[0])-5*(math.log(cosmo.luminosity_distance(z).to(u.pc).value/10 ,10))
            specObj.append(row[12])
            x.append(x_val)
            y.append(y_val)
            redshift_array.append(z)
    
                
table = np.array([specObj,x,y,redshift_array])
np.save('/home/calum/Documents/MPhysProj/data/master_db_tbl.npy',table)
            
