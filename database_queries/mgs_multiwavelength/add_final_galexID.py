#/usr/bin/python

import mx.ODBC.unixODBC as odbc
import numpy as np

# Connect to the database
db = odbc.DriverConnect("DSN=ramses17;UID=wsaro;PWD=wsaropw")

# Initiate the Cursor
cursor = db.cursor()

# Add galexID column to the table ##########################################
# Execute the Query
cursor.execute("ALTER TABLE cmurray..mgs_multiwavelength ADD galexID bigint;") 

# Add galexIDs into the table
# query for galexID
cursor.execute("					\
UPDATE cmurray..mgs_multiwavelength 			\
SET cmurray..mgs_multiwavelength.galexID = x.slaveObjID	\
FROM cmurray..mgs_multiwavelength as m 		\
	INNER JOIN UKIDSSDR10PLUS..lasSourceXGR6PhotoObjAll AS x \
	on m.ukidssID=x.masterObjID				\
 	INNER JOIN GalexGR6..photoObjAll as p		\
 	on p.objID = x.slaveObjID  			\
	WHERE x.distanceMins < 0.0666667			\
	AND x.distanceMins IN (SELECT MIN(distanceMins) \
		FROM UKIDSSDR10PLUS..lasSourceXGR6PhotoObjAll	\
		WHERE masterObjID = x.masterObjID)	\
	AND x.distanceMins IN (SELECT MIN(distanceMins) \
		FROM UKIDSSDR10PLUS..lasSourceXGR6PhotoObjAll	\
		WHERE slaveObjid = p.objID)")

 
# show table (WHERE lasID != 0 does not matter)
cursor.execute("SELECT COUNT(galexID), COUNT(DISTINCT galexID)	\
		FROM cmurray..mgs_multiwavelength")

# Get the results
rows = cursor.fetchall()

print('galexID:',rows)

# Commit the change
db.commit()
# Close the database connection
db.close()
