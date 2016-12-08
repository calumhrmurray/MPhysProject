# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 10:26:56 2016

@author: calum
"""
import numpy as np
import matplotlib.pyplot as plt


array = np.load('/home/calum/Documents/MPhysProj/data/contour_plot.npy')
y1 = array[1]
array = np.load('/home/calum/Documents/MPhysProj/data/vespa_data/vespa_smf_0.1_contour.npy')
y2 = array[1]
array = np.load('/home/calum/Documents/MPhysProj/data/vespa_data/vespa_smf_0.8_contour.npy')
y3 = array[1]
array = np.load('/home/calum/Documents/MPhysProj/data/vespa_data/vespa_smf_0.9_contour.npy')
y4 = array[1]
array = np.load('/home/calum/Documents/MPhysProj/data/vespa_data/vespa_smf_0.95_contour.npy')
y5 = array[1]
array = np.load('/home/calum/Documents/MPhysProj/data/vespa_data/vespa_smf_0.99_contour.npy')
y6 = array[1]

def plot_hist(array):
    weights = np.ones_like(array)/len(array)
    n, bins, patches = plt.hist(array,bins=100,weights=weights)
    return n, bins

plt.figure()
n3, bins = plot_hist(y3) 
n1, bins = plot_hist(y1) 
n2, bins = plot_hist(y2) 
n4, bins = plot_hist(y4) 
n5, bins = plot_hist(y5) 
n6, bins = plot_hist(y6) 

bins = bins[1:]

plt.figure()
plt.plot(bins,n1,label='Full sample')
plt.plot(bins,n2,label='0.1 SMF')
plt.plot(bins,n3,label='0.8 SMF')
plt.plot(bins,n4,label='0.9 SMF')
plt.plot(bins,n5,label='0.95 SMF')
plt.plot(bins,n6,label='0.99 SMF')
plt.xlabel('(u-r)model')

plt.legend()