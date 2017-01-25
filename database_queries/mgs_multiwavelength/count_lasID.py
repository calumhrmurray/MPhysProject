#/usr/bin/python

import mx.ODBC.unixODBC as odbc
import numpy as np

# Connect to the database
db = odbc.DriverConnect("DSN=ramses17;UID=wsaro;PWD=wsaropw")

# Initiate the Cursor
cursor = db.cursor()

# query for lasID and count
cursor.execute("SELECT COUNT(x.masterObjID)	\
	FROM UKIDSSDR10PLUS..lasSourceXDR8PhotoObj AS x 	\
 	WHERE x.masterObjID IS NULL;")

# Get the results
rows = cursor.fetchall()

print(rows)

# Commit the change
#db.commit()
# Close the database connection
db.close()
