#/usr/bin/python

# Sample script for connecting to SDSS DR9, running a query, and printing results

import mx.ODBC.unixODBC as odbc
import numpy as np
import sys

# Connect to the database
db = odbc.DriverConnect("DSN=ramses17;Database=cmurray;UID=wsaro;PWD=wsaropw")

# Initiate the Cursor
cursor = db.cursor()

# Execute the Query
sql_cmd = 'DROP TABLE '+sys.argv[1]+' ;'
cursor.execute(sql_cmd) 

# Commit the cahnge
db.commit()
# Close the database connection
db.close()
