#/usr/bin/python

import mx.ODBC.unixODBC as odbc
import numpy as np

# Connect to the database
db = odbc.DriverConnect("DSN=ramses17;UID=wsaro;PWD=wsaropw")

# Initiate the Cursor
cursor = db.cursor()
 
# show table links, large
cursor.execute("SELECT gal.m_stellar, gal.m_stellar_error, SUM(hr.mass)/115. , 	\
			d.dustVal, SUM(hr.Z)/5., m.z, zoo.p_el_debiased, zoo.p_cs_debiased,	\
			zoo.p_mg,		\
			sdss.u, sdss.g, sdss.r, sdss.i, sdss.z,			\
			sdss.modelMagErr_u ,sdss.modelMagErr_g , sdss.modelMagErr_r,	\
			sdss.modelMagErr_i, sdss.modelMagErr_z,			\
			sdss.petroMag_r, sdss.petroR50_r			\
		FROM cmurray..mgs_multiwavelength as m			\
			INNER JOIN  BestDR13..galaxy AS sdss		\
			on m.specObjID = sdss.specObjID			\
 			INNER JOIN BestDR13..PhotoObjDR7 as dr7		\
 			on sdss.ObjID = dr7.dr8ObjID			\
			INNER JOIN BestDR13..zooSpec as zoo		\
			on sdss.ObjID = zoo.ObjID			\
			INNER JOIN VESPA..lookUpTable as l		\
			on dr7.specObjID = l.specObjID			\
				INNER JOIN VESPA..GalProp as gal		\
				on l.indexP = gal.indexP			\
				INNER JOIN VESPA..DustProp as d			\
				on l.indexP = d.indexP				\
				INNER JOIN VESPA..HRBinProp as hr		\
				on l.indexP = hr.indexP				\
				INNER JOIN VESPA..BinProp as bin		\
				on l.indexP = bin.indexP			\
				AND gal.runID = 4				\
				AND d.runID = 4					\
				AND d.dustID = 2				\
				AND hr.runID = 4				\
				AND hr.binID < 5				\
			GROUP BY m.specObjID, gal.m_stellar, gal.m_stellar_error, \
				d.dustVal, m.z, zoo.p_el_debiased, zoo.p_cs_debiased, \
				zoo.p_mg,		\
				sdss.u, sdss.g, sdss.r, sdss.i, sdss.z,		\
				sdss.modelMagErr_u ,sdss.modelMagErr_g , sdss.modelMagErr_r,	\
				sdss.modelMagErr_i, sdss.modelMagErr_z, \
				sdss.petroMag_r, sdss.petroR50_r ")

# Get the results
rows = cursor.fetchall()

print('Result:', len(rows))

print(rows[0][4],rows[100][4],rows[1000][4],rows[50][4],rows[3][4])

# save results in numpy array
np.save('/home/cmurray/data/final_vespa_properties.npy',rows)

# Close the database connection
db.close()
