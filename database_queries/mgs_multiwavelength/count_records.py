#/usr/bin/python

import mx.ODBC.unixODBC as odbc
import numpy as np

# Connect to the database
db = odbc.DriverConnect("DSN=ramses17;UID=wsaro;PWD=wsaropw")

# Initiate the Cursor
cursor = db.cursor()

# just gets ra and dec for every value in each of the tables!

# Execute the Query
sql_string = 'SELECT COUNT (wise.ra) FROM WISE..wise_allskysc as wise; ' 
	
cursor.execute(sql_string)

print('Cursor executed')

rows = cursor.fetchall()

print('WISE results fetched',rows)

##################################

# Execute the Query
sql_string = 'SELECT COUNT (dec) FROM BestDR13..photoObjAll; ' 
	
cursor.execute(sql_string)

print('Cursor executed')

rows = cursor.fetchall()

print('SDSS results fetched',rows)


#####################################

# Execute the Query
sql_string = 'SELECT COUNT (p.dec) FROM GalexGR6..photoObjAll as p; ' 
	
cursor.execute(sql_string)

print('Cursor executed')

rows = cursor.fetchall()

print('GALEX results fetched',rows)

#####################################

# Execute the Query
sql_string = 'SELECT COUNT (dec) FROM UKIDSSDR10PLUS..lasSource as las; ' 
	
cursor.execute(sql_string)

print('Cursor executed')

rows = cursor.fetchall()

print('UKIDDS LAS results fetched',rows)


# Close the database connection
db.close()
