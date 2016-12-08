#/usr/bin/python

# Sample script for connecting to SDSS DR9, running a query, and printing results

import mx.ODBC.unixODBC as odbc
import numpy as np

# Connect to the database
db = odbc.DriverConnect("DSN=ramses17;Database=BestDR13;UID=wsaro;PWD=wsaropw")

# Initiate the Cursor
cursor = db.cursor()

# Execute the Query
#cursor.execute("SELECT galaxy.petroMag_r,galaxy.modelMag_u,galaxy.modelMag_g,galaxy.modelMag_r,galaxy.modelMag_i,galaxy.modelMag_z, specObj.z FROM galaxy, specObj where galaxy.objID = specObj.bestObjID AND galaxy.primTarget = 0x00000040")

cursor.execute("SELECT g.petroMag_r, s.z, g.modelMag_u, g.modelMag_g, g.modelMag_r, g.modelMag_i,g.modelMag_z, g.modelMagErr_u ,g.modelMagErr_g , g.modelMagErr_i,g.modelMagErr_r, g.modelMagErr_z    \
 FROM galaxy as g 									\
 JOIN specObj as s 									\
  on g.specObjID = s.specObjID 								\
 JOIN ZooNoSpec as zns									\
  on g.objid = zns.objid								\
WHERE (zns.p_cw >0.8 OR zns.p_acw >0.8)")

# Get the results
rows = cursor.fetchall()

# array to store results
results_array = []

# length of data obtained
print(len(rows))

# save results in numpy array
np.save('/home/cmurray/data/galaxy_zoo/spirals_array.npy',rows)

# Close the database connection
db.close()
