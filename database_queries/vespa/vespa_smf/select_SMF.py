#/usr/bin/python

# Sample script for connecting to SDSS DR9, running a query, and printing results

import mx.ODBC.unixODBC as odbc
import numpy as np
import sys

# Connect to the database
db = odbc.DriverConnect("DSN=ramses8;UID=wsaro;PWD=wsaropw")

# Initiate the Cursor
cursor = db.cursor()

# query for a specific stellar mass formation percentage in the last age bin
sql_query = "SELECT g.petroMag_r, s.z, g.modelMag_u, g.modelMag_g, g.modelMag_r, g.modelMag_i,g.modelMag_z, g.modelMagErr_u ,g.modelMagErr_g , g.modelMagErr_i,g.modelMagErr_r, g.modelMagErr_z 				\
FROM BestDR9..galaxy as g 			\
 INNER JOIN BestDR9..PhotoObjDR7 as dr7 	\
 on dr7.dr8objid=g.objID 			\
 INNER JOIN BestDR9..specObj as s 		\
 on s.specObjID= g.specObjID  			\
 INNER JOIN VESPA..lookuptable as l		\
 on l.specObjID = dr7.specObjID			\
 INNER JOIN VESPA..GalProp as gal		\
 on l.indexp = gal.indexp			\
 INNER JOIN VESPA..BinProp as b			\
 on gal.indexp=b.indexp				\
 INNER JOIN VESPA..binID as bID			\
 on bid.binid = b.binID				\
 WHERE s.primTarget=0x00000040			\
 AND bid.ageEnd = 14 AND b.mass > ("+sys.argv[1]+" * gal.m_stellar)			\
 AND gal.m_stellar < 1e14					\
 AND gal.m_stellar > 1e7					\
 AND gal.runID = 2						\
 AND b.runID = 2"

# Execute the Query
cursor.execute(sql_query)

print("Cursor executed")

# Get the results
rows = cursor.fetchall()

print("Results gotten")

# save results in numpy array
np.save('/home/cmurray/data/vespa_SMF_'+sys.argv[1]+'.npy',rows)

# Close the database connection
db.close()
