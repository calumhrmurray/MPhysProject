#/usr/bin/python

# only u,r, mr petro, z, petroR50_r (to calculate surface brightness)

import mx.ODBC.unixODBC as odbc
import numpy as np

# Connect to the database
db = odbc.DriverConnect("DSN=ramses17;UID=wsaro;PWD=wsaropw")

# Initiate the Cursor
cursor = db.cursor()

# get all MGS in ukidds marked as extended source ##########################################
cursor.execute("SELECT sdss.modelMag_u, sdss.modelMag_r, mr_petro, m.z, sdss.petroR50_r \
		FROM cmurray..mgs_multiwavelength as m			\
 			INNER JOIN UKIDSSDR10PLUS..lasSource AS ukidds	\
 			on m.ukidds_largeID = ukidds.sourceID 		\
			INNER JOIN  BestDR13..galaxy AS sdss		\
			on m.specObjID = sdss.specObjID			\
				WHERE mergedClass = +1")

# Get the results
rows = cursor.fetchall()

print('Result:', len(rows))

# save results in numpy array
np.save('/home/cmurray/data/ukidss_extended_source.npy',rows)

# get all MGS in ukidds not marked as extended source ##########################################
cursor.execute("SELECT sdss.modelMag_u, sdss.modelMag_r, mr_petro, m.z, sdss.petroR50_r \
		FROM cmurray..mgs_multiwavelength as m			\
 			INNER JOIN UKIDSSDR10PLUS..lasSource AS ukidds	\
 			on m.ukidds_largeID = ukidds.sourceID 		\
			INNER JOIN  BestDR13..galaxy AS sdss		\
			on m.specObjID = sdss.specObjID			\
				WHERE mergedClass != +1")

# Get the results
rows = cursor.fetchall()

print('Result:', len(rows))

# save results in numpy array
np.save('/home/cmurray/data/ukidss_xextended_source.npy',rows)


# Close the database connection #############################################
db.close()
