# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 10:42:51 2016

@author: calum
"""

import math
from astropy.cosmology import FlatLambdaCDM
import astropy.units as u
import numpy as np
import matplotlib.pyplot as plt
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
    
#tbl = pd.read_csv('/home/calum/QA_data/large_MGS_sample.csv') 
#array = tbl.as_matrix()

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
    invar = pow(0.4*math.log(10)*maggies*np.array(row[7:-2]),-2) 
    k_tuple = np.concatenate(([row[1]],maggies,invar))
    kcorrect_tuple = kcorrect.fit_coeffs(k_tuple)
    k_coeff = kcorrect.reconstruct_maggies(kcorrect_tuple)
    final_input = maggies/np.array(k_coeff[1:])
    kcorrection_array = [-2.5*math.log(item,10) for item in final_input]
    # put above in a function probs 
    y_val = float(row[2]) - kcorrection_array[1] - float(row[4]) + kcorrection_array[3]
    z = k_coeff[0]
    if y_val > 0 and y_val < 3.5:
        if z > 0.004 and z < 0.080:
            x_val = float(row[0])-5*(math.log(cosmo.luminosity_distance(z).to(u.pc).value/10 ,10))
            if x_val < -15.5 and x_val > -23.5: 
                x.append(x_val)
                y.append(y_val)
                
contour_plot_array = np.array([x,y])
                
np.save('/home/calum/Documents/MPhysProj/data/contour_plot.npy',contour_plot_array)
            
print('...finished for loop')

print('Number of galaxies used:',len(x))

# start with a rectangular figure
plt.figure()


ax = plt.axes()

plt.contour

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
#ax.hist2d(x,y,bins=150)
ax.contour(xbins, ybins, vals.T, 20, colors='k', zorder=10)
ax.set_xlim([-23,-16])
ax.set_ylim([0,3.5])
ax.set_xlabel('M r,petro')
ax.set_ylabel('(u-r)model')
title_str = 'Observed bivariate distribution of the sample in rest-frame color vs. \
absolute magnitude. Sample size '+str(len(x))+' galaxies. Colour plot 150 bins, Contour 30 bins.'
ax.set_title(title_str)

plt.draw()

#V = [10,50,100,200,400,800,1200,1400,1600,1700,1800,1900,2000,2050,2100,2150,2200,2225,2250,2275,2300,2320,2340,2360]
#plt.figure()
#CS = plt.contour(xbins, ybins, vals.T, V)
#fmt = ticker.LogFormatterMathtext()
#fmt.create_dummy_axis()
#plt.clabel(CS, CS.levels, fmt=fmt)
#
#plt.show()

#plt.savefig('/home/calum/Documents/MPhysProj/graphs/graphy_mcgraphface')

#plt.figure()
#
#CS = plt.contour(X, Y, 100**Z, locator=plt.LogLocator())
#fmt = ticker.LogFormatterMathtext()
#fmt.create_dummy_axis()
#plt.clabel(CS, CS.levels, fmt=fmt)
#plt.title("$100^Z$")
#
#plt.show()