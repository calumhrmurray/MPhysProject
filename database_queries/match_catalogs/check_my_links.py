#/usr/bin/python

# Sample script for connecting to SDSS DR9, running a query, and printing results

import mx.ODBC.unixODBC as odbc
import numpy as np

# Connect to the database
db = odbc.DriverConnect("DSN=ramses17;UID=wsaro;PWD=wsaropw")

# Initiate the Cursor
cursor = db.cursor()

# query for a specific stellar mass formation percentage in the last age bin
sql_query = "SELECT dr7.ra, dr7.dec, s.ra, s.dec	\
FROM cmurray..MGS_contour_tbl as m 		\
 INNER JOIN BestDR13..specObj as s		\
 on s.specObjID = m.specObjID  			\
 INNER JOIN BestDR13..PhotoObjDR7 as dr7 	\
 on dr7.dr8objid=s.bestObjID "	
			
# Execute the Query
cursor.execute(sql_query)

print("Cursor executed")

# Get the results
rows = cursor.fetchall()

print("Results gotten")

# save results in numpy array
np.save('/home/cmurray/data/check_my_links.npy',rows)

# Close the database connection
db.close()
