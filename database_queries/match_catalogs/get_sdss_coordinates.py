#/usr/bin/python

import mx.ODBC.unixODBC as odbc
from astropy.io import fits
import os

# Connect to the database
db = odbc.DriverConnect("DSN=ramses17;UID=wsaro;PWD=wsaropw")

# Initiate the Cursor
cursor = db.cursor()

# just gets ra and dec for every value in each of the tables

# Execute the Query
sql_string = 'SELECT ra, dec, objID FROM BestDR13..photoObjAll; ' 
	
cursor.execute(sql_string)

print('Cursor executed')

# Get the results and save to array
if os.path.exists('/home/cmurray/data/sdss_coords.fits'):
    os.remove('/home/cmurray/data/sdss_coords.fits')

ra_array = []
dec_array = []
obj_array = []

for row in cursor:
	ra_array.append(row[0])
	dec_array.append(row[1])
	obj_array.append(row[2])	
    
tbhdu = fits.BinTableHDU.from_columns(				       \
		[fits.Column(name='RA', format='E', array=ra_array),   \
		fits.Column(name='DEC', format='E', array=dec_array),  \
		fits.Column(name='OBJ', format='K', array=obj_array)])

tbhdu.writeto('/home/cmurray/data/sdss_coords.fits')

print('SDSS results fetched')


# Close the database connection
db.close()
