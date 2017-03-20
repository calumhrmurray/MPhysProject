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
	INNER JOIN UKIDSSDR10PLUS..lasSourceXwise_allskysc AS x \
	on m.ukidssID=x.masterObjID				\
 	INNER JOIN UKIDSSDR10PLUS..lasSource as las	\
 	on las.sourceID = x.masterObjID		\
 	INNER JOIN WISE..wise_allskysc as p		\
 	on p.cntr = x.slaveObjID  			\
	WHERE x.distanceMins IN (SELECT MIN(distanceMins) \
		FROM UKIDSSDR10PLUS..lasSourceXwise_allskysc	\
		WHERE masterObjID = x.masterObjID)		\
	AND x.distanceMins IN (SELECT MIN(distanceMins) \
		FROM UKIDSSDR10PLUS..lasSourceXwise_allskysc	\
		WHERE slaveObjid = p.cntr) ' 
	
cursor.execute(sql_string)

print('Cursor executed')

# Get the results
rows = cursor.fetchall()

print('Results fetched', len(rows))

# save results in numpy array
np.save('/home/cmurray/data/xmatch_nearest_wise.npy',rows)

# small sample ######################################
# Execute the Query
sql_string = 'SELECT x.slaveObjID, x.distanceMins, p.ra, p.dec, las.ra, las.dec, m.z \
FROM cmurray..mgs_multiwavelength as m 		\
	INNER JOIN UKIDSSDR10PLUS..lasSourceXwise_allskysc AS x \
	on m.ukidssID=x.masterObjID				\
 	INNER JOIN UKIDSSDR10PLUS..lasSource as las	\
 	on las.sourceID = x.masterObjID		\
 	INNER JOIN WISE..wise_allskysc as p		\
 	on p.cntr = x.slaveObjID  			\
	WHERE x.distanceMins < 0.004 AND x.distanceMins IN (SELECT MIN(distanceMins) \
		FROM UKIDSSDR10PLUS..lasSourceXwise_allskysc as in_x	\
		WHERE in_x.masterObjID = m.ukidssID); ' 
	
cursor.execute(sql_string)

print('Cursor executed')

# Get the results
rows = cursor.fetchall()

print('Results fetched', len(rows))

# save results in numpy array
np.save('/home/cmurray/data/xmatch_small_wise.npy',rows)

# large sample ######################################
# Execute the Query
sql_string = 'SELECT x.slaveObjID, x.distanceMins, p.ra, p.dec, las.ra, las.dec, m.z \
FROM cmurray..mgs_multiwavelength as m 		\
	INNER JOIN UKIDSSDR10PLUS..lasSourceXwise_allskysc AS x \
	on m.ukidssID=x.masterObjID				\
 	INNER JOIN UKIDSSDR10PLUS..lasSource as las	\
 	on las.sourceID = x.masterObjID		\
 	INNER JOIN WISE..wise_allskysc as p		\
 	on p.cntr = x.slaveObjID  			\
	WHERE x.distanceMins < 0.008 AND x.distanceMins IN (SELECT MIN(distanceMins) \
		FROM UKIDSSDR10PLUS..lasSourceXwise_allskysc as in_x	\
		WHERE in_x.masterObjID = m.ukidssID); ' 
	
cursor.execute(sql_string)

print('Cursor executed')

# Get the results
rows = cursor.fetchall()

print('Results fetched', len(rows))

# save results in numpy array
np.save('/home/cmurray/data/xmatch_large_wise.npy',rows)

# Close the database connection
db.close()
