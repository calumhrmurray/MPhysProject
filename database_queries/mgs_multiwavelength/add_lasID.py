#/usr/bin/python

import mx.ODBC.unixODBC as odbc
import numpy as np

# Connect to the database
db = odbc.DriverConnect("DSN=ramses17;UID=wsaro;PWD=wsaropw")

# Initiate the Cursor
cursor = db.cursor()

# Add lasID column to the table ##########################################
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
	WHERE x.distanceMins IN (SELECT MIN(distanceMins) \
		FROM UKIDSSDR10PLUS..lasSourceXDR8PhotoObj as in_x	\
		WHERE in_x.slaveObjid = m.objID);")

 
# show table (WHERE lasID != 0 does not matter)
cursor.execute("SELECT COUNT(lasID), COUNT(DISTINCT lasID)	\
		FROM cmurray..mgs_multiwavelength")

# Get the results
rows = cursor.fetchall()

print('lasID:',rows)

# Add ukidds_largeID column to the table ##########################################
# Execute the Query
cursor.execute("ALTER TABLE cmurray..mgs_multiwavelength ADD ukidds_largeID bigint;") 

# Add ukidds_largeID into the table
# query for lasID
cursor.execute("					\
UPDATE cmurray..mgs_multiwavelength 			\
SET cmurray..mgs_multiwavelength.ukidds_largeID = x.masterObjID	\
FROM cmurray..mgs_multiwavelength as m 		\
 	INNER JOIN UKIDSSDR10PLUS..lasSourceXDR8PhotoObj AS x 	\
 	on m.objID=x.slaveObjid			\
	WHERE x.distanceMins < 0.008 AND x.distanceMins IN (SELECT MIN(distanceMins) \
		FROM UKIDSSDR10PLUS..lasSourceXDR8PhotoObj as in_x	\
		WHERE in_x.slaveObjid = m.objID);")

 
# show table 
cursor.execute("SELECT COUNT(ukidds_largeID), COUNT(DISTINCT ukidds_largeID)	\
		FROM cmurray..mgs_multiwavelength")

# Get the results
rows = cursor.fetchall()

print('ukidds_largeID:',rows)


# Add ukidds_smallID column to the table ##########################################
# Execute the Query
cursor.execute("ALTER TABLE cmurray..mgs_multiwavelength ADD ukidds_smallID bigint;") 

# Add ukidds_smallID into the table
# query for lasID
cursor.execute("					\
UPDATE cmurray..mgs_multiwavelength 			\
SET cmurray..mgs_multiwavelength.ukidds_smallID = x.masterObjID	\
FROM cmurray..mgs_multiwavelength as m 		\
 	INNER JOIN UKIDSSDR10PLUS..lasSourceXDR8PhotoObj AS x 	\
 	on m.objID=x.slaveObjid			\
	WHERE x.distanceMins < 0.004 AND x.distanceMins IN (SELECT MIN(distanceMins) \
		FROM UKIDSSDR10PLUS..lasSourceXDR8PhotoObj as in_x	\
		WHERE in_x.slaveObjid = m.objID);")

 
# show table 
cursor.execute("SELECT COUNT(ukidds_smallID), COUNT(DISTINCT ukidds_smallID)	\
		FROM cmurray..mgs_multiwavelength")

# Get the results
rows = cursor.fetchall()

print('ukidds_smallID',rows)


# Commit the change
db.commit()
# Close the database connection
db.close()
