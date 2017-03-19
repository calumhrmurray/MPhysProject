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
			specObjID bigint,				\
			objID bigint,				\
			petroMag_r real,			\
			z real,				\
			ur_colour real);") 
# load dataset
data_tbl = np.load('/home/cmurray/data/final_mgs_array.npy')
#data_tbl = data_tbl.T
# throw data into table
cursor.executemany("INSERT INTO mgs_multiwavelength (specObjID, objID, petroMag_r, z, ur_colour) \
			VALUES (?, ?, ?, ?, ?);", map(tuple, data_tbl.tolist()))


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
cursor.execute("SELECT COUNT(DISTINCT ObjID) FROM cmurray..mgs_multiwavelength")
# Get the results
print(cursor.fetchall())

# show table
cursor.execute("SELECT COUNT(DISTINCT specObjID) FROM cmurray..mgs_multiwavelength")
# Get the results
print(cursor.fetchall())

# Commit the change
db.commit()
# Close the database connection
db.close()


