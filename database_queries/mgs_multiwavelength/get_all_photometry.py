#/usr/bin/python

import mx.ODBC.unixODBC as odbc
import numpy as np

# Connect to the database
db = odbc.DriverConnect("DSN=ramses17;UID=wsaro;PWD=wsaropw")

# Initiate the Cursor
cursor = db.cursor()
 
# show table links, large
cursor.execute("SELECT 	galex.fuv_mag, galex.nuv_mag,  \
		sdss.modelMag_u, sdss.modelMag_g, sdss.modelMag_r, 		\
		sdss.modelMag_i,sdss.modelMag_z,				\
		ukidss.yPetroMag, ukidss.j_1PetroMag, ukidss.hPetroMag, ukidss.kPetroMag, \
		wise.w1mpro ,  wise.w2mpro , wise.w3mpro ,  wise.w4mpro , \
		galex.fuv_magerr, galex.nuv_magerr,				\
		sdss.modelMagErr_u ,sdss.modelMagErr_g , sdss.modelMagErr_r,	\
		sdss.modelMagErr_i, sdss.modelMagErr_z,	\
		ukidss.yPetroMagErr, ukidss.j_1PetroMagErr, ukidss.hPetroMagErr, \
		ukidss.kPetroMagErr, 		\
		wise.w1sigmpro, wise.w2sigmpro, wise.w3sigmpro, wise.w4sigmpro,	\
		mr_petro, m.z			\
		FROM cmurray..mgs_multiwavelength as m			\
 			INNER JOIN UKIDSSDR10PLUS..lasSource AS ukidss	\
 			on m.ukidds_largeID = ukidss.sourceID 		\
			INNER JOIN WISE..wise_allskysc AS wise 		\
			on m.wise_largeID = wise.cntr			\
			INNER JOIN GalexGR6..photoObjAll AS galex 	\
			on m.galex_largeID = galex.objID		\
			INNER JOIN  BestDR13..galaxy AS sdss		\
			on m.specObjID = spec.specObjID")

# Get the results
rows = cursor.fetchall()

print('Result:', len(rows))

# save results in numpy array
np.save('/home/cmurray/data/multiwavelength_magnitudes.npy',rows)

# Close the database connection
db.close()
