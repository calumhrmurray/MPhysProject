#/usr/bin/python

import mx.ODBC.unixODBC as odbc
import numpy as np

# Connect to the database
db = odbc.DriverConnect("DSN=ramses17;UID=wsaro;PWD=wsaropw")

# Initiate the Cursor
cursor = db.cursor()

# query for lasID and count
cursor.execute("SELECT COUNT(x.masterObjID)	\
	FROM cmurray..mgs_multiwavelength as m 		\
	INNER JOIN BestDR13..specObj AS s		\
	on s.specObjID = m.specObjID 			\
 	INNER JOIN UKIDSSDR10PLUS..lasSourceXDR8PhotoObj AS x 	\
 	on s.bestObjID=x.slaveObjid			\
 	INNER JOIN UKIDSSDR10PLUS..lasSource as las	\
 	on las.sourceID = x.masterObjID		\
	WHERE distanceMins IN (			\
 		SELECT MIN(distanceMins)		\
		FROM UKIDSSDR10PLUS..lasSourceXDR8PhotoObj	\
		WHERE masterObjID = x.masterObjID) ;")

# Get the results
rows = cursor.fetchall()

print(rows)

# query for lasID and count
cursor.execute("SELECT COUNT(x.masterObjID)	\
	FROM cmurray..mgs_multiwavelength as m 		\
 	INNER JOIN UKIDSSDR10PLUS..lasSourceXDR8PhotoObj AS x 	\
 	on m.objID=x.slaveObjid			\
 	INNER JOIN UKIDSSDR10PLUS..lasSource as las	\
 	on las.sourceID = x.masterObjID		\
	WHERE x.distanceMins < 0.008 AND distanceMins IN (			\
 		SELECT MIN(distanceMins)		\
		FROM UKIDSSDR10PLUS..lasSourceXDR8PhotoObj	\
		WHERE masterObjID = x.masterObjID) ;")

# Get the results
rows = cursor.fetchall()

print(rows)

# query for lasID and count
cursor.execute("SELECT COUNT(x.masterObjID)	\
	FROM cmurray..mgs_multiwavelength as m 		\
 	INNER JOIN UKIDSSDR10PLUS..lasSourceXDR8PhotoObj AS x 	\
 	on m.objID=x.slaveObjid			\
 	INNER JOIN UKIDSSDR10PLUS..lasSource as las	\
 	on las.sourceID = x.masterObjID		\
	WHERE x.distanceMins < 0.004 AND distanceMins IN (			\
 		SELECT MIN(distanceMins)		\
		FROM UKIDSSDR10PLUS..lasSourceXDR8PhotoObj	\
		WHERE masterObjID = x.masterObjID) ;")

# Get the results
rows = cursor.fetchall()

print(rows)



# Commit the change
#db.commit()
# Close the database connection
db.close()
