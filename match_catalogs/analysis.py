# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 15:10:50 2016

@author: calum
"""

import numpy as np
import matplotlib.pyplot as plt
import math

def plot_hist(array,bin_num):
    weights = np.ones_like(array)/len(array)
    n, bins, patches = plt.hist(array,bins=bin_num,weights=weights)
    plt.close()
    return bins, n

def ra_dec_scatter(filename, bounds=None, img_name = 'null'):
    
    # load array
    array = np.load(filename)
    
    data = []
    
    # get the data    
    for row in array:
        del_ra = row[2]-row[4]
        del_dec = row[3]-row[5]
        data.append([del_ra,del_dec*math.cos(row[3])])
        
    plt.figure(figsize=(20,20))
    plt.plot([row[0] for row in data],[row[1] for row in data],'+')
    plt.ylim(-bounds,bounds)
    plt.xlim(-bounds,bounds)
    plt.savefig('/home/calum/Documents/MPhysProj/match_catalogs/images/'+img_name)
    
    print(img_name)
    
def distance_profiles(filename,nbins=200,title='Distance profile, number of objects:', img_name='null'):
    
    # load array
    array = np.load(filename)    
    
    bins, n = plot_hist([row[1] for row in array],nbins)

    step = 0.5*(bins[1]-bins[0])
    
    plt.figure(figsize=(20,10))
    plt.plot(bins[:-1]+step, n)
    plt.xlabel('Distance (arcminutes)')
    plt.ylabel('Frequency')
    title_str= title+str(len(array))
    plt.title(title_str)
    plt.savefig('/home/calum/Documents/MPhysProj/match_catalogs/images/'+img_name)

plt.close()    

ra_dec_scatter('/home/calum/Documents/Mphys_data/match_catalogs/sdss_neighbours.npy',0.004)
ra_dec_scatter('/home/calum/Documents/Mphys_data/match_catalogs/galex_neighbours.npy',0.004)
ra_dec_scatter('/home/calum/Documents/Mphys_data/match_catalogs/wise_neighbours.npy',0.004)