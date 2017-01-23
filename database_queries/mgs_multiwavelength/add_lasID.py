#/usr/bin/python

import mx.ODBC.unixODBC as odbc
import numpy as np

# Connect to the database
db = odbc.DriverConnect("DSN=ramses17;UID=wsaro;PWD=wsaropw")

# Initiate the Cursor
cursor = db.cursor()

# Add lasID column to the table
# Execute the Query
cursor.execute("ALTER TABLE cmurray..mgs_multiwavelength ADD lasID bigint;") 

# Add lasIDs into the table
# query for lasID
cursor.execute("					\
UPDATE cmurray..mgs_multiwavelength 			\
SET m.lasID = x.masterObjID	\
FROM cmurray..mgs_multiwavelength as m 		\
 	INNER JOIN UKIDSSDR10PLUS..lasSourceXDR8PhotoObj AS x 	\
 	on m.objID=x.slaveObjid			\
 	INNER JOIN UKIDSSDR10PLUS..lasSource as las	\
 	on las.sourceID = x.masterObjID		\
	WHERE distanceMins IN (			\
 		SELECT MIN(distanceMins)		\
		FROM UKIDSSDR10PLUS..lasSourceXDR8PhotoObj	\
		WHERE masterObjID = x.masterObjID);")
 
# show table (WHERE lasID != 0 does not matter)
cursor.execute("SELECT COUNT(lasID) 			\
		FROM cmurray..mgs_multiwavelength")

# Get the results
rows = cursor.fetchall()

print(rows)

# show table (WHERE lasID != 0 does not matter)
cursor.execute("SELECT COUNT(*) 			\
		FROM cmurray..mgs_multiwavelength")

# Get the results
rows = cursor.fetchall()

print(rows)


# Commit the change
#db.commit()
# Close the database connection
db.close()
