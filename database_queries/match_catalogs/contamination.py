#/usr/bin/python

import mx.ODBC.unixODBC as odbc
import numpy as np

# Connect to the database
db = odbc.DriverConnect("DSN=ramses17;UID=wsaro;PWD=wsaropw")

# Initiate the Cursor
cursor = db.cursor()

# Execute the Query
sql_string = 'SELECT TOP 1000000 x.slaveObjID, x.distanceMins	\
FROM UKIDSSDR10PLUS..lasSourceNeighbours as x			\
WHERE x.distanceMins IN (SELECT MIN(distanceMins) 		\
		FROM UKIDSSDR10PLUS..lasSourceXDR8PhotoObj as in_x	\
		WHERE in_x.masterObjID = x.masterObjID) ' 
	
cursor.execute(sql_string)

print('Cursor executed')

# Get the results
rows = cursor.fetchall()

print('Results fetched', len(rows))

# save results in numpy array
np.save('/home/cmurray/data/contamination.npy',rows)

# Close the database connection
db.close()