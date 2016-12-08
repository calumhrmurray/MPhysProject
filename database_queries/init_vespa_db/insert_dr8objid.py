#/usr/bin/python

# Sample script for connecting to SDSS DR9, running a query, and printing results

import mx.ODBC.unixODBC as odbc
import numpy as np

# Connect to the database
db = odbc.DriverConnect("DSN=ramses17;UID=wsaro;PWD=wsaropw")

# Initiate the Cursor
cursor = db.cursor()

# Execute the Query
cursor.execute("SELECT ;") 
# load dataset
data_tbl = np.load('/home/cmurray/data/db_tbl/MGS_contour_tbl.npy')
# throw data into table
cursor.executemany("INSERT INTO MGS_contour_tbl (specObjID, uMinusrColour, Mr_petro, z) \
			VALUES (?, ?, ?, ?);", map(tuple, data_tbl.tolist()))
# Commit the cahnge
db.commit()
# Close the database connection
db.close()
