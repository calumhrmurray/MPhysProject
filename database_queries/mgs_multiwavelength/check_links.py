#/usr/bin/python

import mx.ODBC.unixODBC as odbc
import numpy as np

# Connect to the database
db = odbc.DriverConnect("DSN=ramses17;UID=wsaro;PWD=wsaropw")

# Initiate the Cursor
cursor = db.cursor()
 
# show table links, large
cursor.execute("SELECT COUNT(specObjID)	\
		FROM cmurray..mgs_multiwavelength			\
		WHERE ukidds_largeID IS NOT NULL			\
		AND galex_largeID IS NOT NULL				\
		AND wise_largeID IS NOT NULL")

# Get the results
rows = cursor.fetchall()

print('Result:',rows)

# show table links, small 
cursor.execute("SELECT COUNT(specObjID)	\
		FROM cmurray..mgs_multiwavelength			\
		WHERE ukidds_smallID IS NOT NULL			\
		AND galex_smallID IS NOT NULL				\
		AND wise_smallID IS NOT NULL")

# Get the results
rows = cursor.fetchall()

print('Result:',rows)

# Close the database connection
db.close()
