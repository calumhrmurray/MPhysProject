#/usr/bin/python

# Sample script for connecting to SDSS DR9, running a query, and printing results

import mx.ODBC.unixODBC as odbc
import numpy as np
import sys

# Connect to the database
db = odbc.DriverConnect("DSN=ramses8;UID=wsaro;PWD=wsaropw")

# Initiate the Cursor
cursor = db.cursor()

# query for a specific stellar formation rate
sql_query = "SELECT MIN(g.petroMag_r), MIN(s.z), MIN(g.modelMag_u), MIN(g.modelMag_g), MIN(g.modelMag_r), MIN(g.modelMag_i),MIN(g.modelMag_z), MIN(g.modelMagErr_u) ,MIN(g.modelMagErr_g) , MIN(g.modelMagErr_i),MIN(g.modelMagErr_r), MIN(g.modelMagErr_z), SUM(hr.mass)/115.    \
FROM VESPA..lookUpTable as l				  \
	JOIN VESPA..hrBinProp as hr			  \
	 ON l.indexP = hr.indexP			  \
	JOIN VESPA..binID as bID			  \
	 ON bID.binID = hr.binID			 \
 	JOIN BestDR9..PhotoObjDR7 as dr7		\
 	 ON l.specObjID = dr7.specObjID			\
	JOIN BestDR9..galaxy as g 	\
 	 ON dr7.dr8objid=g.objID			\
	JOIN BestDR9..specObj as s			\
	 ON s.specObjID= g.specObjID 			\
WHERE hr.binID < 5					   \
AND hr.runID = 4				\
AND s.primTarget=0x00000040		\
GROUP BY s.specObjID"		

# Execute the Query
cursor.execute(sql_query)

print("Cursor executed")

# Get the results
rows = cursor.fetchall()

print("Results gotten",len(rows))


# save results in numpy array
np.save('/home/cmurray/data/vespa_SMF_'+sys.argv[1]+'.npy',rows)

# Close the database connection
db.close()
