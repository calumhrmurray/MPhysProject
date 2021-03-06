#/usr/bin/python

import mx.ODBC.unixODBC as odbc
import numpy as np

# Connect to the database
db = odbc.DriverConnect("DSN=ramses17;UID=wsaro;PWD=wsaropw")

# Initiate the Cursor
cursor = db.cursor()
 
# show table links, large
cursor.execute("SELECT ukidds.yPetroMag, ukidds.yPetroMagErr,ukidds.hPetroMag, ukidds.hPetroMagErr, \
			 ukidds.kPetroMag, ukidds.kPetroMagErr, 		\
		wise.w1mpro , wise.w1sigmpro, wise.w2mpro , wise.w2sigmpro,	\
		wise.w3mpro , wise.w3sigmpro, wise.w4mpro , wise.w4sigmpro,	\
		galex.nuv_mag, galex.nuv_magerr, galex.fuv_mag, galex.fuv_magerr, \
		sdss.modelMag_u, sdss.modelMag_g, sdss.modelMag_r, 		\
		sdss.modelMag_i,sdss.modelMag_z,				\
		sdss.modelMagErr_u ,sdss.modelMagErr_g , sdss.modelMagErr_r,	\
		sdss.modelMagErr_i, sdss.modelMagErr_z, mr_petro, m.z			\
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
np.save('/home/cmurray/data/first_all_colours.npy',rows)

# Close the database connection
db.close()
