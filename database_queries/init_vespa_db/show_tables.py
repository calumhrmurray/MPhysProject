#/usr/bin/python

import mx.ODBC.unixODBC as odbc
import numpy as np
import sys

# Connect to the database
connection_cmd = 'DSN=ramses17;Database='+sys.argv[1]+';UID=wsaro;PWD=wsaropw'
db = odbc.DriverConnect(connection_cmd)

# Initiate the Cursor
cursor = db.cursor()

# Execute the Query
cursor.execute("SELECT TABLE_NAME \
FROM INFORMATION_SCHEMA.TABLES		\
WHERE TABLE_TYPE = 'BASE TABLE'")

# Get the results
rows = cursor.fetchall()

for row in rows:
	print(row)

# Close the database connection
db.close()


