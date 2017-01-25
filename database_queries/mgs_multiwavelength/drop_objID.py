#/usr/bin/python

import mx.ODBC.unixODBC as odbc
import numpy as np

# Connect to the database
db = odbc.DriverConnect("DSN=ramses17;UID=wsaro;PWD=wsaropw")

# Initiate the Cursor
cursor = db.cursor()

# Removing bestObjID so we can add fluxObjID better for extended objects
# Execute the Query
cursor.execute("ALTER TABLE cmurray..mgs_multiwavelength DROP COLUMN objID ;") 

# show table
cursor.execute("SELECT TOP 10 * FROM cmurray..mgs_multiwavelength")

# Get the results
rows = cursor.fetchall()

print(rows)

# Commit the change
db.commit()
# Close the database connection
db.close()