#/usr/bin/python

import mx.ODBC.unixODBC as odbc
import numpy as np

# Connect to the database
db = odbc.DriverConnect("DSN=ramses17;UID=wsaro;PWD=wsaropw")

# Initiate the Cursor
cursor = db.cursor()

# just gets ra and dec for every value in each of the tables

# Execute the Query
sql_string = 'SELECT s.ra, s.dec FROM BestDR13..photoObjAll as s; ' 
	
cursor.execute(sql_string)

print('Cursor executed')

rows = []
# Get the results
row = cursor.fetchone()
while row is not None:
	rows.append(cursor.fetchone())

print('SDSS results fetched')

# save results in numpy array
np.save('/home/cmurray/data/sdss_catalog.npy',rows)

# Close the database connection
db.close()
