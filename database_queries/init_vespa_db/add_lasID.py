#/usr/bin/python

import mx.ODBC.unixODBC as odbc
import numpy as np

# Connect to the database
db = odbc.DriverConnect("DSN=ramses17;UID=wsaro;PWD=wsaropw")

# Initiate the Cursor
cursor = db.cursor()

# remove old lasID column
cursor.execute("ALTER TABLE cmurray..MGS_contour_tbl DROP COLUMN lasID;") 
# Add lasID column to the table
# Execute the Query
cursor.execute("ALTER TABLE cmurray..MGS_contour_tbl ADD lasID bigint;") 
# add large sample LasID which will contain more spurious detections
cursor.execute("ALTER TABLE cmurray..MGS_contour_tbl ADD lsLasID bigint;") 
# Add lasIDs into the table
# query for lasID
cursor.execute("					\
UPDATE cmurray..MGS_contour_tbl  			\
 SET cmurray..MGS_contour_tbl.lasID = x.masterObjID	\
 FROM cmurray..MGS_contour_tbl				\
 INNER JOIN BestDR13..specObj as s		\
  on s.specObjID = cmurray..MGS_contour_tbl.specObjID  			\
 INNER JOIN UKIDSSDR10PLUS..lasSourceXDR8PhotoObj AS x 	\
  on s.bestObjID=x.slaveObjid			\
 WHERE x.distanceMins<0.005 AND distanceMins IN (	\
 	SELECT MIN(distanceMins) FROM UKIDSSDR10PLUS..lasSourceXDR8PhotoObj WHERE masterObjID = x.masterObjID	\
						 ) ;")

# Add lsLasIDs into the table
# query for lasID
cursor.execute("					\
UPDATE cmurray..MGS_contour_tbl  			\
 SET cmurray..MGS_contour_tbl.lsLasID = x.masterObjID	\
 FROM cmurray..MGS_contour_tbl				\
 INNER JOIN BestDR13..specObj as s		\
  on s.specObjID = cmurray..MGS_contour_tbl.specObjID  			\
 INNER JOIN UKIDSSDR10PLUS..lasSourceXDR8PhotoObj AS x 	\
  on s.bestObjID=x.slaveObjid			\
 WHERE x.distanceMins<0.01 AND distanceMins IN (	\
 	SELECT MIN(distanceMins)		\
	FROM UKIDSSDR10PLUS..lasSourceXDR8PhotoObj	\
	WHERE masterObjID = x.masterObjID) ;")
 
# show table
cursor.execute("SELECT TOP 20 * \
FROM cmurray..MGS_contour_tbl")

# Get the results
rows = cursor.fetchall()

print(rows)

# Commit the change
db.commit()
# Close the database connection
db.close()

