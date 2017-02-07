#/usr/bin/python

import mx.ODBC.unixODBC as odbc
import numpy as np

# Connect to the database
db = odbc.DriverConnect("DSN=ramses17;UID=wsaro;PWD=wsaropw")

# Initiate the Cursor
cursor = db.cursor()


# nearest ###########################################
# Execute the Query
sql_string = 'SELECT x.slaveObjID, x.distanceMins, s.ra, s.dec, las.ra, las.dec, m.z \
FROM cmurray..mgs_multiwavelength as m 		\
 	INNER JOIN BestDR13..specObj as s		\
 	on s.specObjID = m.specObjID  			\
 	INNER JOIN UKIDSSDR10PLUS..lasSourceXDR8PhotoObj AS x 	\
 	on m.objID=x.slaveObjid			\
 	INNER JOIN UKIDSSDR10PLUS..lasSource as las	\
 	on las.sourceID = x.masterObjID		\
	WHERE x.distanceMins IN (SELECT MIN(distanceMins) \
		FROM UKIDSSDR10PLUS..lasSourceXDR8PhotoObj as in_x	\
		WHERE in_x.masterObjID = x.masterObjID	\
		AND in_x.slaveObjID = m.objID)	 ' 
	
cursor.execute(sql_string)

print('Cursor executed')

# Get the results
rows = cursor.fetchall()

print('Results fetched', len(rows))

# save results in numpy array
np.save('/home/cmurray/data/xmatch_nearest_sdss.npy',rows)

# small sample ######################################
# Execute the Query
sql_string = 'SELECT x.slaveObjID, x.distanceMins, s.ra, s.dec, las.ra, las.dec, m.z \
FROM cmurray..mgs_multiwavelength as m 		\
 	INNER JOIN BestDR13..specObj as s		\
 	on s.specObjID = m.specObjID  			\
 	INNER JOIN UKIDSSDR10PLUS..lasSourceXDR8PhotoObj AS x 	\
 	on m.objID=x.slaveObjid			\
 	INNER JOIN UKIDSSDR10PLUS..lasSource as las	\
 	on las.sourceID = x.masterObjID		\
	WHERE x.distanceMins < 0.004 AND x.distanceMins IN (SELECT MIN(distanceMins) \
		FROM UKIDSSDR10PLUS..lasSourceXDR8PhotoObj as in_x	\
		WHERE in_x.slaveObjid = m.objID); ' 
	
cursor.execute(sql_string)

print('Cursor executed')

# Get the results
rows = cursor.fetchall()

print('Results fetched', len(rows))

# save results in numpy array
np.save('/home/cmurray/data/xmatch_small_sdss.npy',rows)

# large sample ######################################
# Execute the Query
sql_string = 'SELECT x.slaveObjID, x.distanceMins, s.ra, s.dec, las.ra, las.dec, m.z \
FROM cmurray..mgs_multiwavelength as m 		\
 	INNER JOIN BestDR13..specObj as s		\
 	on s.specObjID = m.specObjID  			\
 	INNER JOIN UKIDSSDR10PLUS..lasSourceXDR8PhotoObj AS x 	\
 	on m.objID=x.slaveObjid			\
 	INNER JOIN UKIDSSDR10PLUS..lasSource as las	\
 	on las.sourceID = x.masterObjID		\
	WHERE x.distanceMins < 0.008 AND x.distanceMins IN (SELECT MIN(distanceMins) \
		FROM UKIDSSDR10PLUS..lasSourceXDR8PhotoObj as in_x	\
		WHERE in_x.slaveObjid = m.objID) ' 
	
cursor.execute(sql_string)

print('Cursor executed')

# Get the results
rows = cursor.fetchall()

print('Results fetched', len(rows))

# save results in numpy array
np.save('/home/cmurray/data/xmatch_large_sdss.npy',rows)

# Close the database connection
db.close()
