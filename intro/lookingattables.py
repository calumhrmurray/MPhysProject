# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 15:55:14 2016

@author: calum
"""

from astropy.io import fits
from numpy import rec

f = fits.open('/home/calum/Documents/MPhysProj/intro/GalaxyZoo1_DR_table3.fits')
tbldata = f[1].header

print(f[0].header)
print(tbldata)