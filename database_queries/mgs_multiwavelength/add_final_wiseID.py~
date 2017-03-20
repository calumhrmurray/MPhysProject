#/usr/bin/python

import mx.ODBC.unixODBC as odbc
import numpy as np

# Connect to the database
db = odbc.DriverConnect("DSN=ramses17;UID=wsaro;PWD=wsaropw")

# Initiate the Cursor
cursor = db.cursor()

# Add wiseID column to the table ##########################################
# Execute the Query
cursor.execute("ALTER TABLE cmurray..mgs_multiwavelength ADD wiseID bigint;") 

# Add galexIDs into the table
# query for galexID
cursor.execute("					\
UPDATE cmurray..mgs_multiwavelength 			\
SET cmurray..mgs_multiwavelength.wiseID = x.slaveObjID	\
FROM cmurray..mgs_multiwavelength as m 		\
	INNER JOIN UKIDSSDR10PLUS..lasSourceXwise_allskysc AS x \
	on m.ukidssID=x.masterObjID				\
 	INNER JOIN WISE..wise_allskysc as wise		\
 	on wise.cntr = x.slaveObjID  			\
	WHERE x.distanceMins < 0.0133333			\
	AND x.distanceMins IN (SELECT MIN(distanceMins) \
		FROM UKIDSSDR10PLUS..lasSourceXwise_allskysc	\
		WHERE masterObjID = x.masterObjID)	\
	AND x.distanceMins IN (SELECT MIN(distanceMins) \
		FROM UKIDSSDR10PLUS..lasSourceXwise_allskysc	\
		WHERE slaveObjid = wise.cntr)")

 
# show table (WHERE lasID != 0 does not matter)
cursor.execute("SELECT COUNT(wiseID), COUNT(DISTINCT wiseID)	\
		FROM cmurray..mgs_multiwavelength")

# Get the results
rows = cursor.fetchall()

print('wiseID:',rows)

# Commit the change
db.commit()
# Close the database connection
db.close()
