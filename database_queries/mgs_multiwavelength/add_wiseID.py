#/usr/bin/python

import mx.ODBC.unixODBC as odbc
import numpy as np

# Connect to the database
db = odbc.DriverConnect("DSN=ramses17;UID=wsaro;PWD=wsaropw")

# Initiate the Cursor
cursor = db.cursor()

# Add galexID column to the table ##########################################
# Execute the Query
cursor.execute("ALTER TABLE cmurray..mgs_multiwavelength ADD wiseID bigint;") 

# Add galexIDs into the table
# query for galexID
cursor.execute("					\
UPDATE cmurray..mgs_multiwavelength 			\
SET cmurray..mgs_multiwavelength.wiseID = x.slaveObjID	\
FROM cmurray..mgs_multiwavelength as m 		\
	INNER JOIN UKIDSSDR10PLUS..lasSourceXwise_allskysc AS x \
	on m.lasID=x.masterObjID				\
	WHERE x.distanceMins IN (SELECT MIN(distanceMins) \
		FROM UKIDSSDR10PLUS..lasSourceXwise_allskysc as in_x	\
		WHERE in_x.masterObjID = m.lasID);")

 
# show table (WHERE lasID != 0 does not matter)
cursor.execute("SELECT COUNT(wiseID), COUNT(DISTINCT wiseID)	\
		FROM cmurray..mgs_multiwavelength")

# Get the results
rows = cursor.fetchall()

print('wiseID:',rows)

# Add galex_largeID column to the table ##########################################
# Execute the Query
cursor.execute("ALTER TABLE cmurray..mgs_multiwavelength ADD wise_largeID bigint;") 

# Add galex_largeID into the table
# query for lasID
cursor.execute("					\
UPDATE cmurray..mgs_multiwavelength 			\
SET cmurray..mgs_multiwavelength.wise_largeID = x.slaveObjID	\
FROM cmurray..mgs_multiwavelength as m 		\
	INNER JOIN UKIDSSDR10PLUS..lasSourceXwise_allskysc AS x \
	on m.lasID=x.masterObjID				\
	WHERE x.distanceMins < 0.008				\
	AND x.distanceMins IN (SELECT MIN(distanceMins) \
		FROM UKIDSSDR10PLUS..lasSourceXwise_allskysc as in_x	\
		WHERE in_x.masterObjID = m.lasID);")

 
# show table 
cursor.execute("SELECT COUNT(wise_largeID), COUNT(DISTINCT wise_largeID)	\
		FROM cmurray..mgs_multiwavelength")

# Get the results
rows = cursor.fetchall()

print('wise_largeID:',rows)


# Add galex_smallID column to the table ##########################################
# Execute the Query
cursor.execute("ALTER TABLE cmurray..mgs_multiwavelength ADD wise_smallID bigint;") 

# Add galex_smallID into the table
# query for lasID
cursor.execute("					\
UPDATE cmurray..mgs_multiwavelength 			\
SET cmurray..mgs_multiwavelength.wise_smallID = x.slaveObjID	\
FROM cmurray..mgs_multiwavelength as m 		\
	INNER JOIN UKIDSSDR10PLUS..lasSourceXwise_allskysc AS x \
	on m.lasID=x.masterObjID				\
	WHERE x.distanceMins < 0.004				\
	AND x.distanceMins IN (SELECT MIN(distanceMins) \
		FROM UKIDSSDR10PLUS..lasSourceXwise_allskysc as in_x	\
		WHERE in_x.masterObjID = m.lasID);")

 
# show table 
cursor.execute("SELECT COUNT(wise_smallID), COUNT(DISTINCT wise_smallID)	\
		FROM cmurray..mgs_multiwavelength")

# Get the results
rows = cursor.fetchall()

print('wise_smallID',rows)


# Commit the change
db.commit()
# Close the database connection
db.close()
