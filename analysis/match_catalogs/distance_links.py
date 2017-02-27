# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 11:23:23 2016

@author: calum
"""

import numpy as np
import matplotlib.pyplot as plt
from astropy import units as u
from astropy.coordinates import SkyCoord

def plot_hist(array,bin_num):
    weights = np.ones_like(array)/len(array)
    n, bins, patches = plt.hist(array,bins=bin_num,weights=weights)
    plt.close()
    return bins, n

#link_array = np.load('/home/calum/Documents/Mphys_data/match_catalogs/check_my_links.npy')
#print(link_array.shape)
#
#hist_array = []
#
#for row in link_array:
#    dr7_coord = SkyCoord(ra=row[0]*u.degree, dec=row[1]*u.degree)
#    dr13_coord = SkyCoord(ra=row[2]*u.degree, dec=row[3]*u.degree)
#    sep = dr7_coord.separation(dr13_coord)
#    hist_array.append(sep.radian)
#    
#print(len(hist_array))

np.load('/home/calum/Documents/Mphys_data/match_catalogs/hist_array.npy')

bins, n = plot_hist(hist_array,200)

step = 0.5*(bins[1]-bins[0])

plt.figure(figsize=(20,10))
plt.plot(bins[:-1]+step, n)
