#/usr/bin/python

import mx.ODBC.unixODBC as odbc
import numpy as np

# Connect to the database
db = odbc.DriverConnect("DSN=ramses17;UID=wsaro;PWD=wsaropw")

# Initiate the Cursor
cursor = db.cursor()

# query for lasID and count
cursor.execute("SELECT COUNT(dr2.bestObjID), COUNT(DISTINCT dr2.bestObjID), COUNT(las.sourceID), \
		COUNT(DISTINCT las.sourceID), COUNT(x.masterObjID), COUNT(DISTINCT x.masterObjID) \
FROM UKIDSSDR10PLUS..lasSource AS las, BestDR13..specObj AS dr2, UKIDSSDR10PLUS..lasSourceXDR8PhotoObj AS x		\
WHERE masterObjID=las.sourceID AND slaveObjID=dr2.bestObjID AND distanceMins<0.033333 	\
AND dr2.sdssPrimary=1 AND distanceMins IN (		\
SELECT MIN(distanceMins) 		\
FROM UKIDSSDR10PLUS..lasSourceXDR8PhotoObj					\
WHERE masterObjID=x.masterObjID );")

# Get the results
rows = cursor.fetchall()

print(rows)

# Close the database connection
db.close()
