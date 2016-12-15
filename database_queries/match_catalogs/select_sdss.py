#/usr/bin/python

import mx.ODBC.unixODBC as odbc
import numpy as np

# Connect to the database
db = odbc.DriverConnect("DSN=ramses17;UID=wsaro;PWD=wsaropw")

# Initiate the Cursor
cursor = db.cursor()

# Execute the Query
sql_string = 'SELECT x.slaveObjID, x.distanceMins, s.ra, s.dec, las.ra, las.dec, m.z \
FROM cmurray..MGS_contour_tbl as m 		\
 INNER JOIN BestDR13..specObj as s		\
 on s.specObjID = m.specObjID  			\
 INNER JOIN UKIDSSDR10PLUS..lasSourceXDR8PhotoObj AS x 	\
 on s.bestObjID=x.slaveObjid			\
 INNER JOIN UKIDSSDR10PLUS..lasSource as las	\
 on las.sourceID = x.masterObjID' 
	
cursor.execute(sql_string)

print('Cursor executed')

# Get the results
rows = cursor.fetchall()

print('Results fetched')

# save results in numpy array
np.save('/home/cmurray/data/sdss_neighbours.npy',rows)

# Close the database connection
db.close()

