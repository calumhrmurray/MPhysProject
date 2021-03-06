#/usr/bin/python

import mx.ODBC.unixODBC as odbc
import numpy as np

# Connect to the database
db = odbc.DriverConnect("DSN=ramses17;UID=wsaro;PWD=wsaropw")

# Initiate the Cursor
cursor = db.cursor()

# nearest ###########################################
# Execute the Query
sql_string = 'SELECT COUNT(objID) FROM GalexGR6..photoObjAll ' 
	
cursor.execute(sql_string)

print('Cursor executed')

# Get the results
rows = cursor.fetchall()

print('Results fetched', rows)

# nearest ###########################################
# Execute the Query
sql_string = 'SELECT COUNT(slaveObjID), COUNT(DISTINCT slaveObjID),COUNT(DISTINCT lasID), \
		COUNT(lasID)								  \
FROM cmurray..mgs_multiwavelength as m 		\
	INNER JOIN UKIDSSDR10PLUS..lasSourceXGR6PhotoObjAll AS x \
	on m.lasID=x.masterObjID				\
 	INNER JOIN UKIDSSDR10PLUS..lasSource as las	\
 	on las.sourceID = x.masterObjID		\
 	INNER JOIN GalexGR6..photoObjAll as p		\
 	on p.objID = x.slaveObjID  			\
	WHERE x.distanceMins IN (SELECT MIN(distanceMins) \
		FROM UKIDSSDR10PLUS..lasSourceXGR6PhotoObjAll as in_x	\
		WHERE in_x.masterObjID = m.lasID); ' 
	
cursor.execute(sql_string)

print('Cursor executed')

# Get the results
rows = cursor.fetchall()

print('Results fetched', rows)

# small sample ######################################
# Execute the Query
sql_string = 'SELECT COUNT(slaveObjID), COUNT(DISTINCT slaveObjID),COUNT(DISTINCT lasID), \
		COUNT(lasID)								  \
FROM cmurray..mgs_multiwavelength as m 		\
	INNER JOIN UKIDSSDR10PLUS..lasSourceXGR6PhotoObjAll AS x \
	on m.lasID=x.masterObjID				\
 	INNER JOIN UKIDSSDR10PLUS..lasSource as las	\
 	on las.sourceID = x.masterObjID		\
 	INNER JOIN GalexGR6..photoObjAll as p		\
 	on p.objID = x.slaveObjID  			\
	WHERE x.distanceMins < 0.004 AND x.distanceMins IN (SELECT MIN(distanceMins) \
		FROM UKIDSSDR10PLUS..lasSourceXGR6PhotoObjAll as in_x	\
		WHERE in_x.masterObjID = m.lasID); ' 
	
cursor.execute(sql_string)

print('Cursor executed')

# Get the results
rows = cursor.fetchall()

print('Results fetched', rows)

# large sample ######################################
# Execute the Query
sql_string = 'SELECT COUNT(slaveObjID), COUNT(DISTINCT slaveObjID),COUNT(DISTINCT lasID), \
		COUNT(lasID)								  \
FROM cmurray..mgs_multiwavelength as m 		\
	INNER JOIN UKIDSSDR10PLUS..lasSourceXGR6PhotoObjAll AS x \
	on m.lasID=x.masterObjID				\
 	INNER JOIN UKIDSSDR10PLUS..lasSource as las	\
 	on las.sourceID = x.masterObjID		\
 	INNER JOIN GalexGR6..photoObjAll as p		\
 	on p.objID = x.slaveObjID  			\
	WHERE x.distanceMins < 0.008 AND x.distanceMins IN (SELECT MIN(distanceMins) \
		FROM UKIDSSDR10PLUS..lasSourceXGR6PhotoObjAll as in_x	\
		WHERE in_x.masterObjID = m.lasID); ' 
	
cursor.execute(sql_string)

print('Cursor executed')

# Get the results
rows = cursor.fetchall()

print('Results fetched',rows)

# Close the database connection
db.close()
