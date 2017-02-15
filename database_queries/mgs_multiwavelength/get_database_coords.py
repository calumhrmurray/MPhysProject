#/usr/bin/python

import mx.ODBC.unixODBC as odbc
import numpy as np

# Connect to the database
db = odbc.DriverConnect("DSN=ramses17;UID=wsaro;PWD=wsaropw")

# Initiate the Cursor
cursor = db.cursor()

# just gets ra and dec for every value in each of the tables!

# Execute the Query
sql_string = 'SELECT wise.ra, wise.dec FROM WISE..wise_allskysc as wise; ' 
	
cursor.execute(sql_string)

print('Cursor executed')

rows = []
# Get the results
for row in cursor:
	rows.append(cursor.fetchone())

print('WISE results fetched')

# save results in numpy array
np.save('/home/cmurray/data/wise_catalog.npy',rows)

##################################

# Execute the Query
sql_string = 'SELECT s.ra, s.dec FROM BestDR13..photoObjAll as s; ' 
	
cursor.execute(sql_string)

print('Cursor executed')

rows = []
# Get the results
for row in cursor:
	rows.append(cursor.fetchone())

print('SDSS results fetched')

# save results in numpy array
np.save('/home/cmurray/data/sdss_catalog.npy',rows)

#####################################

# Execute the Query
sql_string = 'SELECT p.ra, p.dec FROM GalexGR6..photoObjAll as p; ' 
	
cursor.execute(sql_string)

print('Cursor executed')

rows = []
# Get the results
for row in cursor:
	rows.append(cursor.fetchone())

print('GALEX results fetched')

# save results in numpy array
np.save('/home/cmurray/data/galex_catalog.npy',rows)

# Close the database connection
db.close()
