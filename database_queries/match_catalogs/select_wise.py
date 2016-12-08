#/usr/bin/python

import mx.ODBC.unixODBC as odbc
import numpy as np

# Connect to the database
db = odbc.DriverConnect("DSN=ramses17;UID=wsaro;PWD=wsaropw")

# Initiate the Cursor
cursor = db.cursor()

# Execute the Query
sql_string = 'SELECT x.slaveObjID, x.distanceMins       \
FROM UKIDSSDR9PLUS..lasSourceXwise_allskysc AS x 	\
INNER JOIN WISE..
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
