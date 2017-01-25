#/usr/bin/python

import mx.ODBC.unixODBC as odbc
import numpy as np

# Connect to the database
db = odbc.DriverConnect("DSN=ramses17;UID=wsaro;PWD=wsaropw")

# Initiate the Cursor
cursor = db.cursor()


# nearest ###########################################
# Execute the Query
sql_string = 'SELECT x.slaveObjID, x.distanceMins, p.ra, p.dec, las.ra, las.dec, m.z \
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

print('Results fetched', len(rows))

# save results in numpy array
np.save('/home/cmurray/data/xmatch_nearest_galex.npy',rows)

# small sample ######################################
# Execute the Query
sql_string = 'SELECT x.slaveObjID, x.distanceMins, p.ra, p.dec, las.ra, las.dec, m.z \
FROM cmurray..mgs_multiwavelength as m 		\
	INNER JOIN UKIDSSDR10PLUS..lasSourceXGR6PhotoObjAll AS x \
	on m.lasID=x.masterObjID				\
 	INNER JOIN UKIDSSDR10PLUS..lasSource as las	\
 	on las.sourceID = x.masterObjID		\
 	INNER JOIN GalexGR6..photoObjAll as p		\
 	on p.objID = x.slaveObjID  			\
	WHERE x.distanceMins < 0.02 AND x.distanceMins IN (SELECT MIN(distanceMins) \
		FROM UKIDSSDR10PLUS..lasSourceXGR6PhotoObjAll as in_x	\
		WHERE in_x.masterObjID = m.lasID); ' 
	
cursor.execute(sql_string)

print('Cursor executed')

# Get the results
rows = cursor.fetchall()

print('Results fetched', len(rows))

# save results in numpy array
np.save('/home/cmurray/data/xmatch_small_galex.npy',rows)

# large sample ######################################
# Execute the Query
sql_string = 'SELECT x.slaveObjID, x.distanceMins, p.ra, p.dec, las.ra, las.dec, m.z \
FROM cmurray..mgs_multiwavelength as m 		\
	INNER JOIN UKIDSSDR10PLUS..lasSourceXGR6PhotoObjAll AS x \
	on m.lasID=x.masterObjID				\
 	INNER JOIN UKIDSSDR10PLUS..lasSource as las	\
 	on las.sourceID = x.masterObjID		\
 	INNER JOIN GalexGR6..photoObjAll as p		\
 	on p.objID = x.slaveObjID  			\
	WHERE x.distanceMins < 0.04 AND x.distanceMins IN (SELECT MIN(distanceMins) \
		FROM UKIDSSDR10PLUS..lasSourceXGR6PhotoObjAll as in_x	\
		WHERE in_x.masterObjID = m.lasID); ' 
	
cursor.execute(sql_string)

print('Cursor executed')

# Get the results
rows = cursor.fetchall()

print('Results fetched', len(rows))

# save results in numpy array
np.save('/home/cmurray/data/xmatch_large_galex.npy',rows)

# Close the database connection
db.close()
