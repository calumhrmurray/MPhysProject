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
sql_string = 'SELECT p.ra, p.dec FROM GalexGR6..photoObjAll as p; ' 


sql_string = 'SELECT x.slaveObjID, x.distanceMins, p.ra, p.dec, las.ra, las.dec, m.z \
	FROM UKIDSSDR10PLUS..lasSource as las	\
 	on las.sourceID = x.masterObjID		\
 	INNER JOIN GalexGR6..photoObjAll as p		\
 	on p.objID = x.slaveObjID  			\
	WHERE x.distanceMins IN (SELECT MIN(distanceMins) \
		FROM UKIDSSDR10PLUS..lasSourceXGR6PhotoObjAll as in_x	\
		WHERE in_x.masterObjID = m.lasID)'
	
cursor.execute(sql_string)

print('Cursor executed')

# Get the results and save to array
if os.path.exists('/home/cmurray/data/ra_galex.gz'):
    os.remove('/home/cmurray/data/ra_galex.gz')
    
if os.path.exists('/home/cmurray/data/dec_galex.gz'):
    os.remove('/home/cmurray/data/dec_galex.gz')

ra=open('/home/cmurray/data/ra_galex.gz','ab')
dec=open('/home/cmurray/data/dec_galex.gz','ab')

for row in cursor:
    np.savetxt(ra,[row[0]])
    np.savetxt(dec,[row[1]])
    
ra.close()
dec.close()

print('GALEX results fetched')


# Close the database connection
db.close()
