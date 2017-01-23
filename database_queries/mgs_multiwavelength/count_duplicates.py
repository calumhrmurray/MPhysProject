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
cursor.execute("SELECT objID, COUNT(*) \
		FROM mgs_multiwavelength \
		GROUP BY objID \
		HAVING COUNT(*) > 1")

# Get the results
rows = cursor.fetchall()

print('Duplicate objiD')
print(rows)
print(len(rows))

# Execute the Query
cursor.execute("SELECT specobjID, COUNT(*) \
		FROM mgs_multiwavelength \
		GROUP BY specobjID \
		HAVING COUNT(*) > 1")

# Get the results
rows = cursor.fetchall()

print('Duplicate specobjiD')
print(rows)
print(len(rows))


# Close the database connection
db.close()
