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
cursor.execute("SELECT * FROM cmurray.INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = N'mgs_multiwavelength'")

# Get the results
rows = cursor.fetchall()

for row in rows:
	print(row)

# Execute the Query
cursor.execute("SELECT TOP 10 * FROM mgs_multiwavelength")

# Get the results
rows = cursor.fetchall()

for row in rows:
	print(row)

# show table
cursor.execute("SELECT COUNT(objID) FROM cmurray..mgs_multiwavelength")
# Get the results
print(cursor.fetchall())

# show table
cursor.execute("SELECT COUNT(specObjID) FROM cmurray..mgs_multiwavelength")
# Get the results
print(cursor.fetchall())



# Close the database connection
db.close()
