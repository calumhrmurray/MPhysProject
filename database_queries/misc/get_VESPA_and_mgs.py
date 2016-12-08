#/usr/bin/python

# Sample script for connecting to SDSS DR9, running a query, and printing results

import mx.ODBC.unixODBC as odbc
import numpy as np

# Connect to the database
db_SDSS = odbc.DriverConnect("DSN=ramses17;Database=BestDR13;UID=wsaro;PWD=wsaropw")
db_VESPA = odbc.DriverConnect("DSN=ramses8;Database=VESPA;UID=wsaro;PWD=wsaropw")

# Initiate the Cursor
cursor_SDSS = db_SDSS.cursor()
cursor_VESPA = db_VESPA.cursor()

# Execute the Query
#cursor.execute("SELECT galaxy.petroMag_r,galaxy.modelMag_u,galaxy.modelMag_g,galaxy.modelMag_r,galaxy.modelMag_i,galaxy.modelMag_z, specObj.z FROM galaxy, specObj where galaxy.objID = specObj.bestObjID AND galaxy.primTarget = 0x00000040")

#cursor_SDSS.execute("SELECT TOP 1 g.petroMag_r,g.modelMag_u,g.modelMag_g,g.modelMag_r, \
#g.modelMag_i,g.modelMag_z, s.z, dr7.dr7objid \
#FROM galaxy as g \
#JOIN PhotoObjDR7 as dr7 on dr7.SpecObjID=g.specObjID \
#JOIN specObj as s on g.objID=s.bestObjID \
#WHERE s.primTarget=0x00000040")


cursor_SDSS.execute("SELECT g.petroMag_r, s.z, g.modelMag_u, g.modelMag_g, g.modelMag_r, g.modelMag_i,g.modelMag_z, g.modelFluxIvar_u ,g.modelFluxIvar_g , g.modelFluxIvar_r,g.modelFluxIvar_i, g.modelFluxIvar_z, dr7.specObjID  \
FROM galaxy as g			\
 INNER JOIN PhotoObjDR7 as dr7		\
 on dr7.dr8objid=g.objID		\
 INNER JOIN specObj as s 		\
 on s.specObjID= g.specObjID		\
WHERE s.primTarget=0x00000040")

print("one works")

# Get the results
rows_SDSS = cursor_SDSS.fetchall()

# create objID array
object_array = []
object_array = [object_row[-1] for object_row in rows_SDSS]

num_none = 0

print("two works")

# output array
output_array = []
rows_VESPA = []

#use the object array to select MGS data from VESPA
for specObjID in object_array:
	sql_command = 'SELECT * FROM lookuptable as l, galProp as g \
WHERE l.specObjID = '+str(specObjID)+' AND l.indexP = g.indexP AND g.runID = 4'
	cursor_VESPA.execute(sql_command)
	row_VESPA = cursor_VESPA.fetchall()
	if row_VESPA == None:
		num_none += 1
	# add VESPA data and MGS data together
	output_array.append(row_VESPA)
	#rows_VESPA.append(row_VESPA)

print('Number of nones:',num_none)

print(len(output_array))

# save results in numpy array
np.save('/home/cmurray/data/VESPA_and_MGS_run4.npy',output_array)
#np.save('/home/cmurray/data/VESPA_run4.npy',rows_VESPA)

# Close the database connection
db_SDSS.close()
db_VESPA.close()
