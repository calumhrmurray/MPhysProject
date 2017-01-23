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
SET cmurray..mgs_multiwavelength.lasID = x.masterObjID	\
	FROM cmurray..mgs_multiwavelength as m 		\
 	INNER JOIN UKIDSSDR10PLUS..lasSourceXDR8PhotoObj AS x 	\
 	on m.objID=x.slaveObjid			\
 	INNER JOIN UKIDSSDR10PLUS..lasSource as las	\
 	on las.sourceID = x.masterObjID		\
	WHERE  (priOrSec <= 0 or priOrSec = frameSetID)				\
	AND    (j_1Class = +1 OR j_1Class = -3) AND j_1ppErrBits < 256		\
	AND    (hClass   = +1 OR hClass = -3) AND hppErrBits < 256		\
	AND    (kClass   = +1 OR kClass = -3) AND kppErrBits < 256		\
	AND    (yClass   = +1 OR yClass = -3 OR yClass = -9999) AND yppErrBits < 256	\
	AND    (j_2Class = +1 OR j_2Class = -3 OR j_2Class = -9999) 		\
	AND j_2ppErrBits < 256							\
 	AND distanceMins < 0.005					\
	AND distanceMins IN (			\
 		SELECT MIN(distanceMins)		\
		FROM UKIDSSDR10PLUS..lasSourceXDR8PhotoObj	\
		WHERE masterObjID = x.masterObjID) ;")
 
# show table
cursor.execute("SELECT COUNT(lasID) 			\
		FROM cmurray..mgs_multiwavelength	\
		WHERE lasID != 0")

# Get the results
rows = cursor.fetchall()

print(rows)

# Commit the change
#db.commit()
# Close the database connection
db.close()
