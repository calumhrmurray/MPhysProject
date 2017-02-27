# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 11:56:17 2016

@author: calum
"""

import numpy as np
import kcorrect
import math

array = np.load('/home/calum/Documents/MPhysProj/mgs_sample/mgs_kcorrect_array.npy')

# set things up
#kcorrect.load_templates()
#kcorrect.load_filters()

#Note that the conversion to the inverse variances from the maggies and the magnitude errors is (0.4 ln(10) × maggies × magerr)-2
# maggies are simply related to magnitudes by 10−0.4m

#−2.5 log10(maggies/maggies.z0)

for row in array[:1]:
    maggies = np.array(pow(10,-0.4*row[2:7]))
    invar = pow(0.4*math.log(10)*maggies*np.array(row[7:]),-2) 
    k_tuple = np.concatenate(([row[1]],maggies,invar))
    kcorrect_tuple = kcorrect.fit_coeffs(k_tuple)
    k_coeff = kcorrect.reconstruct_maggies(kcorrect_tuple)
    final_input = maggies/np.array(k_coeff[1:])
    kcorrection_array = [-2.5*math.log(item,10) for item in final_input]
    


