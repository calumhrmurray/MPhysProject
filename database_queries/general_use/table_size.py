#/usr/bin/python

import mx.ODBC.unixODBC as odbc
import numpy as np
import sys

# Connect to the database
db = odbc.DriverConnect("DSN=ramses17;UID=wsaro;PWD=wsaropw")

# Initiate the Cursor
cursor = db.cursor()

# Execute the Query
sql_string = 'SELECT COUNT(*) FROM '+sys.argv[1]
	
cursor.execute(sql_string)

print('Cursor executed')

# Get the results
rows = cursor.fetchall()

print(rows)

# Close the database connection
db.close()

