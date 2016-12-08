#/usr/bin/python

import mx.ODBC.unixODBC as odbc
import numpy as np

# Connect to the database
db = odbc.DriverConnect("DSN=ramses17;UID=wsaro;PWD=wsaropw")

# Initiate the Cursor
cursor = db.cursor()

# Execute the Query
sql_string = 'SELECT x.slaveObjID, x.distanceMins, s.ra, s.dec, m.z \
FROM cmurray..MGS_contour_tbl as m 		\
 INNER JOIN BestDR13..specObj as s		\
 on s.specObjID = m.specObjID  			\
 INNER JOIN BestDR13..PhotoObjDR7 as dr7 	\
 on dr7.dr8objid=s.bestObjID 			\
 INNER JOIN UKIDSSDR9PLUS..lasSourceXDR8PhotoObj AS x 	\
 on dr7.dr8objid=x.slaveObjid' 
	
cursor.execute(sql_string)

print('Cursor executed')

# Get the results
rows = cursor.fetchall()

print('Results fetched')

# save results in numpy array
np.save('/home/cmurray/data/sdss_neighbours.npy',rows)

# Close the database connection
db.close()

