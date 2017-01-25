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
	on m.lasID=x.masterObjID				\
 	INNER JOIN UKIDSSDR10PLUS..lasSource as las	\
 	on las.sourceID = x.masterObjID		\
	WHERE x.distanceMins IN (SELECT MIN(distanceMins) \
		FROM UKIDSSDR10PLUS..lasSourceXGR6PhotoObjAll as in_x	\
		WHERE in_x.masterObjID = m.lasID);")

 
# show table (WHERE lasID != 0 does not matter)
cursor.execute("SELECT COUNT(galexID), COUNT(DISTINCT galexID)	\
		FROM cmurray..mgs_multiwavelength")

# Get the results
rows = cursor.fetchall()

print('galexID:',rows)

# Add galex_largeID column to the table ##########################################
# Execute the Query
cursor.execute("ALTER TABLE cmurray..mgs_multiwavelength ADD galex_largeID bigint;") 

# Add galex_largeID into the table
# query for lasID
cursor.execute("					\
UPDATE cmurray..mgs_multiwavelength 			\
SET cmurray..mgs_multiwavelength.galex_largeID = x.slaveObjID	\
FROM cmurray..mgs_multiwavelength as m 		\
	INNER JOIN UKIDSSDR10PLUS..lasSourceXGR6PhotoObjAll AS x \
	on m.lasID=x.masterObjID				\
 	INNER JOIN UKIDSSDR10PLUS..lasSource as las	\
 	on las.sourceID = x.masterObjID		\
	WHERE x.distanceMins < 0.04 AND x.distanceMins IN (SELECT MIN(distanceMins) \
		FROM UKIDSSDR10PLUS..lasSourceXGR6PhotoObjAll as in_x	\
		WHERE in_x.masterObjID = m.lasID);")

 
# show table 
cursor.execute("SELECT COUNT(galex_largeID), COUNT(DISTINCT galex_largeID)	\
		FROM cmurray..mgs_multiwavelength")

# Get the results
rows = cursor.fetchall()

print('galex_largeID:',rows)


# Add galex_smallID column to the table ##########################################
# Execute the Query
cursor.execute("ALTER TABLE cmurray..mgs_multiwavelength ADD galex_smallID bigint;") 

# Add galex_smallID into the table
# query for lasID
cursor.execute("					\
UPDATE cmurray..mgs_multiwavelength 			\
SET cmurray..mgs_multiwavelength.galex_smallID = x.slaveObjID	\
FROM cmurray..mgs_multiwavelength as m 		\
	INNER JOIN UKIDSSDR10PLUS..lasSourceXGR6PhotoObjAll AS x \
	on m.lasID=x.masterObjID				\
 	INNER JOIN UKIDSSDR10PLUS..lasSource as las	\
 	on las.sourceID = x.masterObjID		\
	WHERE x.distanceMins < 0.02 AND x.distanceMins IN (SELECT MIN(distanceMins) \
		FROM UKIDSSDR10PLUS..lasSourceXGR6PhotoObjAll as in_x	\
		WHERE in_x.masterObjID = m.lasID);")

 
# show table 
cursor.execute("SELECT COUNT(galex_smallID), COUNT(DISTINCT galex_smallID)	\
		FROM cmurray..mgs_multiwavelength")

# Get the results
rows = cursor.fetchall()

print('galex_smallID',rows)


# Commit the change
#db.commit()
# Close the database connection
db.close()
