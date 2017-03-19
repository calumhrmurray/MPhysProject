#/usr/bin/python

import mx.ODBC.unixODBC as odbc
import numpy as np

# Connect to the database
db = odbc.DriverConnect("DSN=ramses17;UID=wsaro;PWD=wsaropw")

# Initiate the Cursor
cursor = db.cursor()


# nearest ###########################################
# Execute the Query
sql_string = ' \
SELECT x.slaveObjID, x.distanceMins, s.ra, s.dec, las.ra, las.dec, m.z \
FROM cmurray..mgs_multiwavelength as m 		\
 	INNER JOIN BestDR13..specObj as s		\
 	on s.specObjID = m.specObjID  			\
 	INNER JOIN UKIDSSDR10PLUS..lasSourceXDR8PhotoObj AS x 	\
 	on m.objID=x.slaveObjid			\
 	INNER JOIN UKIDSSDR10PLUS..lasSource as las	\
 	on las.sourceID = x.masterObjID		\
	WHERE x.distanceMins IN (SELECT MIN(distanceMins) \
		FROM UKIDSSDR10PLUS..lasSourceXDR8PhotoObj	\
		WHERE masterObjID = x.masterObjID) \
	AND x.distanceMins IN (SELECT MIN(distanceMins) \
		FROM UKIDSSDR10PLUS..lasSourceXDR8PhotoObj	\
		WHERE slaveObjid = m.objID)	 ' 
	
cursor.execute(sql_string)

print('View created')

# Get the results
rows = cursor.fetchall()

for row in rows[:20]:
	print(row[0])

print('Results fetched', len(rows))

# save results in numpy array
np.save('/home/cmurray/data/twocon_xmatch_nearest_sdss.npy',rows)

# nearest ###########################################
# Execute the Query
sql_string = 'SELECT COUNT(DISTINCT s.specObjID), COUNT(DISTINCT m.specObjID), COUNT(DISTINCT m.objID), COUNT(DISTINCT x.masterObjID) \
FROM cmurray..mgs_multiwavelength as m 		\
 	INNER JOIN BestDR13..specObj as s		\
 	on s.specObjID = m.specObjID  			\
 	INNER JOIN UKIDSSDR10PLUS..lasSourceXDR8PhotoObj AS x 	\
 	on m.objID=x.slaveObjid			\
 	INNER JOIN UKIDSSDR10PLUS..lasSource as las	\
 	on las.sourceID = x.masterObjID		\
	WHERE x.distanceMins IN (SELECT MIN(distanceMins) \
		FROM UKIDSSDR10PLUS..lasSourceXDR8PhotoObj	\
		WHERE masterObjID = x.masterObjID)	\
	AND x.distanceMins IN (SELECT MIN(distanceMins) \
		FROM UKIDSSDR10PLUS..lasSourceXDR8PhotoObj	\
		WHERE slaveObjid = m.objID)	 ' 
	
cursor.execute(sql_string)

print('Cursor executed')

# Get the results
rows = cursor.fetchall()

print('Results fetched', rows)


# small sample ######################################
# Execute the Query
sql_string = 'SELECT x.slaveObjID, x.distanceMins, s.ra, s.dec, las.ra, las.dec, m.z, s.specObjID \
FROM cmurray..mgs_multiwavelength as m 		\
 	INNER JOIN BestDR13..specObj as s		\
 	on s.specObjID = m.specObjID  			\
 	INNER JOIN UKIDSSDR10PLUS..lasSourceXDR8PhotoObj AS x 	\
 	on m.objID=x.slaveObjid			\
 	INNER JOIN UKIDSSDR10PLUS..lasSource as las	\
 	on las.sourceID = x.masterObjID		\
	WHERE x.distanceMins < 0.0166667 AND x.distanceMins IN (SELECT MIN(distanceMins) \
		FROM UKIDSSDR10PLUS..lasSourceXDR8PhotoObj as in_x	\
		WHERE in_x.masterObjID = x.masterObjID)		\
	AND x.distanceMins IN (SELECT MIN(distanceMins) \
		FROM UKIDSSDR10PLUS..lasSourceXDR8PhotoObj	\
		WHERE slaveObjid = m.objID) ' 
	
cursor.execute(sql_string)

print('Cursor executed')

# Get the results
rows = cursor.fetchall()

print('Results fetched', len(rows))

# save results in numpy array
np.save('/home/cmurray/data/xmatch_small_sdss.npy',rows)

# small sample ######################################
# Execute the Query
sql_string = 'SELECT COUNT(DISTINCT s.specObjID), COUNT(DISTINCT m.specObjID), COUNT(DISTINCT m.objID), COUNT(DISTINCT x.masterObjID), \
			COUNT(DISTINCT x.slaveObjID) \
FROM cmurray..mgs_multiwavelength as m 		\
 	INNER JOIN BestDR13..specObj as s		\
 	on s.specObjID = m.specObjID  			\
 	INNER JOIN UKIDSSDR10PLUS..lasSourceXDR8PhotoObj AS x 	\
 	on m.objID=x.slaveObjid			\
 	INNER JOIN UKIDSSDR10PLUS..lasSource as las	\
 	on las.sourceID = x.masterObjID		\
	WHERE x.distanceMins < 0.00166667 AND x.distanceMins IN (SELECT MIN(distanceMins) \
		FROM UKIDSSDR10PLUS..lasSourceXDR8PhotoObj as in_x	\
		WHERE in_x.masterObjID = x.masterObjID); ' 
	
cursor.execute(sql_string)

print('Cursor executed')

# Get the results
rows = cursor.fetchall()

print('Results fetched', rows)

# Execute the Query
cursor.execute("SELECT  COUNT(DISTINCT s.specObjID), COUNT(DISTINCT m.specObjID), COUNT(DISTINCT m.objID) \
 FROM cmurray..mgs_multiwavelength as m			\
 JOIN BestDR13..specObj as s		\
 on s.specObjID = m.specObjID	\
 WHERE s.primTarget = 0x00000040")

# Get the results
rows = cursor.fetchall()

print('Results fetched', rows)

# Close the database connection
db.close()
