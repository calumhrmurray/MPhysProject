#/usr/bin/python

import mx.ODBC.unixODBC as odbc
import numpy as np

# Connect to the database
db = odbc.DriverConnect("DSN=ramses17;UID=wsaro;PWD=wsaropw")

# Initiate the Cursor
cursor = db.cursor()
 
# show table links, large
cursor.execute("SELECT m.z, zoo.p_el_debiased, zoo.p_cs_debiased,	\
			sdss.u, sdss.g, sdss.r, sdss.i, sdss.z,			\
			sdss.petroMag_r, sdss.petroR50_r,			\
			ukidds.yPetroMag, ukidds.hPetroMag, ukidds.kPetroMag, 	\
			wise.w1mpro, wise.w2mpro, wise.w3mpro, wise.w4mpro, 	\
			galex.nuv_mag, galex.fuv_mag  				\
		FROM cmurray..mgs_multiwavelength as m			\
			INNER JOIN  BestDR13..galaxy AS sdss		\
			on m.specObjID = sdss.specObjID			\
 			INNER JOIN BestDR13..PhotoObjDR7 as dr7		\
 			on sdss.ObjID = dr7.dr8ObjID			\
			INNER JOIN BestDR13..zooSpec as zoo		\
			on sdss.ObjID = zoo.ObjID			\
			INNER JOIN UKIDSSDR10PLUS..lasSource AS ukidds	\
 			on m.ukidds_largeID = ukidds.sourceID 		\
			INNER JOIN WISE..wise_allskysc AS wise 		\
			on m.wise_largeID = wise.cntr			\
			INNER JOIN GalexGR6..photoObjAll AS galex 	\
			on m.galex_largeID = galex.objID ")

# Get the results
rows = cursor.fetchall()

print('Result:', len(rows))

# save results in numpy array
np.save('/home/cmurray/data/phot_morph.npy',rows)

# Close the database connection
db.close()
