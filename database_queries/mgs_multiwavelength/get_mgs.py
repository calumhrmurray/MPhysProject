#/usr/bin/python

import mx.ODBC.unixODBC as odbc
import numpy as np

# Connect to the database
db = odbc.DriverConnect("DSN=ramses17;Database=BestDR13;UID=wsaro;PWD=wsaropw")

# Initiate the Cursor
cursor = db.cursor()

# Execute the Query
cursor.execute("SELECT  s.specObjID, g.objID, g.petroMag_r, s.z, g.modelMag_u - g.modelMag_r \
 FROM specObj as s			\
 JOIN galaxy as g		\
 on g.specObjID = s.specObjID	\
 WHERE s.primTarget = 0x00000040 \
 AND g.objID = s.bestObjID")

# Get the results
rows = cursor.fetchall()

# array to store results
results_array = []

# length of data obtained
print(len(rows))

rows = np.array(rows,dtype=int)

# save results in numpy array
np.save('/home/cmurray/data/final_mgs_array.npy',rows)

# Close the database connection
db.close()
