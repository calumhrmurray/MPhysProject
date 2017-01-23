#/usr/bin/python

import mx.ODBC.unixODBC as odbc
import numpy as np
import sys

# Connect to the database
connection_cmd = 'DSN=ramses17;Database=cmurray;UID=wsaro;PWD=wsaropw'
db = odbc.DriverConnect(connection_cmd)

# Initiate the Cursor
cursor = db.cursor()


# Execute the Query
cursor.execute("SELECT * FROM sys.triggers")

# Get the results
rows = cursor.fetchall()

print(rows)


# Close the database connection
db.close()
