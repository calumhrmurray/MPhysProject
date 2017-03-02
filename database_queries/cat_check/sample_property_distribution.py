#/usr/bin/python

# this script gets colour information for each galaxy depending on which surveys it is in!
# only u,r, mr petro, z, petroR50_r (to calculate surface brightness)

import mx.ODBC.unixODBC as odbc
import numpy as np

# Connect to the database
db = odbc.DriverConnect("DSN=ramses17;UID=wsaro;PWD=wsaropw")

# Initiate the Cursor
cursor = db.cursor()

# get all MGS ###############################################
cursor.execute("SELECT sdss.modelMag_u, sdss.modelMag_r, mr_petro, m.z, sdss.petroR50_r \
		FROM cmurray..mgs_multiwavelength as m			\
			INNER JOIN  BestDR13..galaxy AS sdss		\
			on m.specObjID = sdss.specObjID")

# Get the results
rows = cursor.fetchall()

print('Result:', len(rows))

# save results in numpy array
np.save('/home/cmurray/data/all_mgs_colours.npy',rows)


# get all MGS in ukidds ##########################################
cursor.execute("SELECT sdss.modelMag_u, sdss.modelMag_r, mr_petro, m.z, sdss.petroR50_r \
		FROM cmurray..mgs_multiwavelength as m			\
 			INNER JOIN UKIDSSDR10PLUS..lasSource AS ukidds	\
 			on m.ukidds_largeID = ukidds.sourceID 		\
			INNER JOIN  BestDR13..galaxy AS sdss		\
			on m.specObjID = sdss.specObjID			\
				WHERE ukidds_largeID IS NOT NULL")

# Get the results
rows = cursor.fetchall()

print('Result:', len(rows))

# save results in numpy array
np.save('/home/cmurray/data/all_ukidss_colours.npy',rows)

# get all MGS in galex ##############################################
cursor.execute("SELECT sdss.modelMag_u, sdss.modelMag_r, mr_petro, m.z, sdss.petroR50_r \
		FROM cmurray..mgs_multiwavelength as m			\
			INNER JOIN GalexGR6..photoObjAll AS galex 	\
			on m.galex_largeID = galex.objID		\
			INNER JOIN  BestDR13..galaxy AS sdss		\
			on m.specObjID = sdss.specObjID			\
				WHERE galex_largeID IS NOT NULL")

# Get the results
rows = cursor.fetchall()

print('Result:', len(rows))

# save results in numpy array
np.save('/home/cmurray/data/all_galex_colours.npy',rows)

# get all MGS in wise #####################################
cursor.execute("SELECT sdss.modelMag_u, sdss.modelMag_r, mr_petro, m.z, sdss.petroR50_r \
		FROM cmurray..mgs_multiwavelength as m			\
			INNER JOIN WISE..wise_allskysc AS wise 		\
			on m.wise_largeID = wise.cntr			\
			INNER JOIN  BestDR13..galaxy AS sdss		\
			on m.specObjID = sdss.specObjID			\
				WHERE wise_largeID IS NOT NULL")

# Get the results
rows = cursor.fetchall()

print('Result:', len(rows))

# save results in numpy array
np.save('/home/cmurray/data/all_wise_colours.npy',rows)

# get all MGS in multiwavelength ###################################
cursor.execute("SELECT sdss.modelMag_u, sdss.modelMag_r, mr_petro, m.z, sdss.petroR50_r \
		FROM cmurray..mgs_multiwavelength as m			\
 			INNER JOIN UKIDSSDR10PLUS..lasSource AS ukidds	\
 			on m.ukidds_largeID = ukidds.sourceID 		\
			INNER JOIN WISE..wise_allskysc AS wise 		\
			on m.wise_largeID = wise.cntr			\
			INNER JOIN GalexGR6..photoObjAll AS galex 	\
			on m.galex_largeID = galex.objID		\
			INNER JOIN  BestDR13..galaxy AS sdss		\
			on m.specObjID = sdss.specObjID			\
				WHERE ukidds_largeID IS NOT NULL	\
				AND galex_largeID IS NOT NULL		\
				AND wise_largeID IS NOT NULL")

# Get the results
rows = cursor.fetchall()

print('Result:', len(rows))

# save results in numpy array
np.save('/home/cmurray/data/all_mw_colours.npy',rows)

# Close the database connection #############################################
db.close()
