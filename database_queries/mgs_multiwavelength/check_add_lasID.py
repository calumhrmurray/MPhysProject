#/usr/bin/python

import mx.ODBC.unixODBC as odbc
import numpy as np

# Connect to the database
db = odbc.DriverConnect("DSN=ramses17;UID=wsaro;PWD=wsaropw")

# Initiate the Cursor
cursor = db.cursor()

# query for lasID and count
cursor.execute("SELECT COUNT(DISTINCT x.masterObjID), COUNT(DISTINCT x.slaveObjID),		\
	 COUNT(m.objID), COUNT(DISTINCT m.objID)	\
	FROM cmurray..mgs_multiwavelength as m 		\
 	INNER JOIN UKIDSSDR10PLUS..lasSourceXDR8PhotoObj AS x 	\
 	on m.objID=x.slaveObjid			\
	WHERE x.distanceMins IN (SELECT MIN(distanceMins) \
		FROM UKIDSSDR10PLUS..lasSourceXDR8PhotoObj as in_x	\
		WHERE in_x.slaveObjid = m.objID		\
		AND in_x.masterObjID = x.masterObjID);")

# Get the results
rows = cursor.fetchall()

print(rows)


# query for lasID and count
cursor.execute("SELECT COUNT(DISTINCT x.masterObjID), COUNT(DISTINCT x.slaveObjID),		\
	 COUNT(m.objID), COUNT(DISTINCT m.objID)	\
	FROM cmurray..mgs_multiwavelength as m 		\
 	INNER JOIN UKIDSSDR10PLUS..lasSourceXDR8PhotoObj AS x 	\
 	on m.objID=x.slaveObjid			\
	WHERE x.distanceMins IN (SELECT MIN(distanceMins) \
		FROM UKIDSSDR10PLUS..lasSourceXDR8PhotoObj as in_x	\
		WHERE in_x.slaveObjid = m.objID		\
		);")

# Get the results
rows = cursor.fetchall()

print(rows)

# query for lasID and count
cursor.execute("SELECT COUNT(DISTINCT x.masterObjID), COUNT(DISTINCT x.slaveObjID),		\
	 COUNT(m.objID), COUNT(DISTINCT m.objID)		\
	FROM cmurray..mgs_multiwavelength as m 		\
 	INNER JOIN UKIDSSDR10PLUS..lasSourceXDR8PhotoObj AS x 	\
 	on m.objID=x.slaveObjid			\
	WHERE x.distanceMins < 0.008 AND x.distanceMins IN (SELECT MIN(distanceMins) \
		FROM UKIDSSDR10PLUS..lasSourceXDR8PhotoObj as in_x	\
		WHERE in_x.slaveObjid = m.objID) ;")

# Get the results
rows = cursor.fetchall()

print(rows)

# query for lasID and count
cursor.execute("SELECT COUNT(DISTINCT x.masterObjID), COUNT(DISTINCT x.slaveObjID),		\
	 COUNT(m.objID), COUNT(DISTINCT m.objID)	\
	FROM cmurray..mgs_multiwavelength as m 		\
 	INNER JOIN UKIDSSDR10PLUS..lasSourceXDR8PhotoObj AS x 	\
 	on m.objID=x.slaveObjid			\
	WHERE x.distanceMins < 0.004 AND x.distanceMins IN (SELECT MIN(distanceMins) \
		FROM UKIDSSDR10PLUS..lasSourceXDR8PhotoObj as in_x	\
		WHERE in_x.slaveObjid = m.objID) ;")

# Get the results
rows = cursor.fetchall()

print(rows)

# Close the database connection
db.close()
