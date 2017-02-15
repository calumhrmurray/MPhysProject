#/usr/bin/python

import mx.ODBC.unixODBC as odbc
import numpy as np
import os

# Connect to the database
db = odbc.DriverConnect("DSN=ramses17;UID=wsaro;PWD=wsaropw")

# Initiate the Cursor
cursor = db.cursor()

# just gets ra and dec for every value in each of the tables

# Execute the Query
sql_string = 'SELECT s.ra, s.dec FROM BestDR13..photoObjAll as s; ' 
	
cursor.execute(sql_string)

print('Cursor executed')

# Get the results and save to array
if os.path.exists('/home/cmurray/data/ra_sdss_catalog.gz'):
    os.remove('/home/cmurray/data/ra_sdss_catalog.gz')
    
if os.path.exists('/home/cmurray/data/dec_sdss_catalog.gz'):
    os.remove('/home/cmurray/data/dec_sdss_catalog.gz')

ra=open('/home/cmurray/data/ra_sdss_catalog.gz','ab')
dec=open('/home/cmurray/data/dec_sdss_catalog.gz','ab')

for row in cursor:
    np.savetxt(ra,[row[0]])
    np.savetxt(dec,[row[1]])
    
ra.close()
dec.close()

print('SDSS results fetched')


# Close the database connection
db.close()
