#/usr/bin/python

# Sample script for connecting to SDSS DR9, running a query, and printing results

import mx.ODBC.unixODBC as odbc
import numpy as np
import sys

# Connect to the database
db = odbc.DriverConnect("DSN=ramses17;Database=cmurray;UID=wsaro;PWD=wsaropw")

# Initiate the Cursor
cursor = db.cursor()

# add stellar mass bin column
# Execute the Query
sql_cmd = "ALTER TABLE MGS_contour_tbl   			\
			ADD stellar_mass_bin_"+sys.argv[1]+" real ;"
cursor.execute(sql_cmd) 


# throw data into column
cursor.execute("INSERT INTO MGS_contour_tbl (specObjID, uMinusrColour, Mr_petro, z) \
			VALUES (?, ?, ?, ?);", map(tuple, data_tbl.tolist()))
# Commit the cahnge
db.commit()
# Close the database connection
db.close()

