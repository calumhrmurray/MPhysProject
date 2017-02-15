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
sql_string = 'SELECT p.ra, p.dec FROM GalexGR6..photoObjAll as p; ' 
	
cursor.execute(sql_string)

print('Cursor executed')

# Get the results and save to array
if os.path.exists('/home/cmurray/data/galex_coords.fits'):
    os.remove('/home/cmurray/data/galex_coords.fits')

ra_array = []
dec_array = []

for row in cursor:
	ra_array.append(row[0])
	dec_array.append(row[1])	
    
tbhdu = fits.BinTableHDU.from_columns(				       \
		[fits.Column(name='RA', format='E', array=ra_array),   \
		fits.Column(name='DEC', format='E', array=dec_array)])

tbhdu.writeto('/home/cmurray/data/galex_coords.fits')

print('GALEX results fetched')


# Close the database connection
db.close()
