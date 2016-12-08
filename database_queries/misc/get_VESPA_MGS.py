#/usr/bin/python

# Sample script for connecting to SDSS DR9, running a query, and printing results

import mx.ODBC.unixODBC as odbc
import numpy as np

# Connect to the database
db_SDSS = odbc.DriverConnect("DSN=ramses8;Database=BestDR13;UID=wsaro;PWD=wsaropw")
db_VESPA = odbc.DriverConnect("DSN=ramses8;Database=VESPA;UID=wsaro;PWD=wsaropw")

# Initiate the Cursor
cursor_SDSS = db_SDSS.cursor()
cursor_VESPA = db_VESPA.cursor()

# Execute the Query
cursor_SDSS.execute("SELECT g.petroMag_r, s.z, g.modelMag_u, g.modelMag_g, g.modelMag_r, g.modelMag_i,g.modelMag_z, g.modelMagErr_u ,g.modelMagErr_g , g.modelMagErr_i,g.modelMagErr_r, g.modelMagErr_z , dr7.specObjID  \
FROM galaxy as g			\
 INNER JOIN PhotoObjDR7 as dr7		\
 on dr7.dr8objid=g.objID		\
 INNER JOIN specObj as s 		\
 on s.specObjID= g.specObjID		\
WHERE s.primTarget=0x00000040")

print("one works")

# Get the results
rows_SDSS = cursor_SDSS.fetchall()

cursor_VESPA.execute("SELECT g.m_stellar, l.specObjID \
FROM GalProp as g					\
  INNER JOIN BinProp as b				\
    ON g.indexp=b.indexp				\
  INNER JOIN binID as bID				\
    ON bid.binid = b.binID				\
  INNER JOIN lookuptable as l \
    ON l.indexp=g.indexp	\
WHERE bid.ageEnd = 14 AND b.mass > (0.5 * g.m_stellar)			\
AND g.m_stellar < 1e14					\
AND g.m_stellar > 1e7					\
AND g.runID = 2						\
AND b.runID = 2")

# Get the results
rows_VESPA = cursor_VESPA.fetchall()

# save results in numpy array
np.save('/home/cmurray/data/MGS_4_smd.npy',rows_SDSS)
np.save('/home/cmurray/data/VESPA_smd.npy',rows_VESPA)

# Close the database connection
db_SDSS.close()
db_VESPA.close()
