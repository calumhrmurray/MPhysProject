#/usr/bin/python

# Sample script for connecting to SDSS DR9, running a query, and printing results

import mx.ODBC.unixODBC as odbc
import numpy as np

# Connect to the database
db = odbc.DriverConnect("DSN=ramses17;Database=cmurray;UID=wsaro;PWD=wsaropw")

# Initiate the Cursor
cursor = db.cursor()

# Execute the Query
cursor.execute("CREATE TABLE mgs_multiwavelength			\
			(					\
			objID bigint,				\
			specObjID bigint,				\
			ur_colour real,			\
			mr_petro real,				\
			z real);") 
# load dataset
data_tbl = np.load('/home/cmurray/data/db_tbl/init_mgs_multiwavelength.npy')
data_tbl = data_tbl.T
# throw data into table
cursor.executemany("INSERT INTO mgs_multiwavelength (objID, specObjID, ur_colour, mr_petro, z) \
			VALUES (?, ?, ?, ?, ?);", map(tuple, data_tbl.tolist()))

# Commit the change
db.commit()
# Close the database connection
db.close()


