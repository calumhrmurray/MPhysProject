#/usr/bin/python

import mx.ODBC.unixODBC as odbc
import numpy as np

# Connect to the database
db = odbc.DriverConnect("DSN=ramses17;Database=cmurray;UID=wsaro;PWD=wsaropw")

# Initiate the Cursor
cursor = db.cursor()

# Execute the Query
#cursor.execute("SELECT TABLE_NAME \
#FROM INFORMATION_SCHEMA.TABLES		\
#WHERE TABLE_TYPE = 'BASE TABLE'")
cursor.execute("SELECT TOP 10 * FROM MGS_contour_tbl")

# Get the results
rows = cursor.fetchall()

for row in rows:
	print(row)

# Close the database connection
db.close()
