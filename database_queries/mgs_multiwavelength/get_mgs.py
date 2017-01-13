#/usr/bin/python

import mx.ODBC.unixODBC as odbc
import numpy as np

# Connect to the database
db = odbc.DriverConnect("DSN=ramses17;Database=BestDR13;UID=wsaro;PWD=wsaropw")

# Initiate the Cursor
cursor = db.cursor()

# Execute the Query
cursor.execute("SELECT g.petroMag_r, s.z, g.modelMag_u, g.modelMag_g, g.modelMag_r, g.modelMag_i,g.modelMag_z, g.modelMagErr_u ,g.modelMagErr_g , g.modelMagErr_i,g.modelMagErr_r, g.modelMagErr_z, s.specObjID, s.bestObjID \
 FROM galaxy as g			\
 INNER JOIN specObj as s		\
 on g.specObjID = s.specObjID	\
 WHERE s.primTarget = 0x00000040")

# Get the results
rows = cursor.fetchall()

# array to store results
results_array = []

# length of data obtained
print(len(rows))

# save results in numpy array
np.save('/home/cmurray/data/final_mgs_array.npy',rows)

# Close the database connection
db.close()
