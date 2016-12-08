#/usr/bin/python

# Sample script for connecting to SDSS DR9, running a query, and printing results

import mx.ODBC.unixODBC as odbc
import numpy as np

# Connect to the database
db = odbc.DriverConnect("DSN=ramses8;Database=VESPA;UID=wsaro;PWD=wsaropw")

# Initiate the Cursor
cursor = db.cursor()

# Execute the Query
#cursor.execute("SELECT galaxy.petroMag_r,galaxy.modelMag_u,galaxy.modelMag_g,galaxy.modelMag_r,galaxy.modelMag_i,galaxy.modelMag_z, specObj.z FROM galaxy, specObj where galaxy.objID = specObj.bestObjID AND galaxy.primTarget = 0x00000040")

#variable
var = [("516080267020")]

cursor.execute("SELECT TOP 10 * FROM lookuptable as l, galProp as g \
WHERE l.specObjID = 75375473458151424 AND l.indexP = g.indexP AND g.runID = 4")

#c.execute("SELECT * FROM foo WHERE bar = %s AND baz = %s", (param1, param2))


# Get the results
rows = cursor.fetchall()

# array to store results
for row in rows:
	print(row)

# Close the database connection
db.close()
