#/usr/bin/python

import mx.ODBC.unixODBC as odbc
import numpy as np

# Connect to the database
db = odbc.DriverConnect("DSN=ramses17;UID=wsaro;PWD=wsaropw")

# Initiate the Cursor
cursor = db.cursor()

# Add ukidssID column to the table ##########################################
# Execute the Query
cursor.execute("ALTER TABLE cmurray..mgs_multiwavelength ADD ukidssID bigint;") 

# Add ukidssID into the table
# query for lasID
cursor.execute("					\
UPDATE cmurray..mgs_multiwavelength 			\
SET cmurray..mgs_multiwavelength.ukidssID = x.masterObjID	\
FROM cmurray..mgs_multiwavelength as m 		\
 	INNER JOIN UKIDSSDR10PLUS..lasSourceXDR8PhotoObj AS x 	\
 	on m.ObjID=x.slaveObjid			\
	WHERE x.distanceMins < 0.0166667 AND x.distanceMins IN (SELECT MIN(distanceMins) \
		FROM UKIDSSDR10PLUS..lasSourceXDR8PhotoObj	\
		WHERE masterObjID = x.masterObjID);")

 
# show table 
cursor.execute("SELECT COUNT(DISTINCT ObjID), COUNT(DISTINCT specObjID),	\
                       COUNT(ukidssID), COUNT(DISTINCT ukidssID)	\
		FROM cmurray..mgs_multiwavelength")

# Get the results
rows = cursor.fetchall()

print('ukidssID:',rows)



# Commit the change
#db.commit()
# Close the database connection
db.close()