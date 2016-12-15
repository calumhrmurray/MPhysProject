#/usr/bin/python

import mx.ODBC.unixODBC as odbc
import numpy as np

# Connect to the database
db = odbc.DriverConnect("DSN=ramses17;UID=wsaro;PWD=wsaropw")

# Initiate the Cursor
cursor = db.cursor()

# Execute the Query
sql_string = 'SELECT x.masterObjID, x.distanceMins, s.ra, s.dec, las.ra, las.dec \
FROM cmurray..MGS_contour_tbl as m 		\
 INNER JOIN UKIDSSDR10PLUS..lasSourceXGR6PhotoObjAll AS x 	\
 on m.lasID=x.masterObjID					\
 INNER JOIN UKIDSSDR10PLUS..lasSource as las			\
 on las.sourceID = x.masterObjID				\
 INNER JOIN GalexGR6..photoobjall as s				\
 on s.objid = x.slaveObjID'  
	
cursor.execute(sql_string)

print('Cursor executed')

# Get the results
rows = cursor.fetchall()

print('Results fetched')

# save results in numpy array
np.save('/home/cmurray/data/galex_neighbours.npy',rows)

# Close the database connection
db.close()
