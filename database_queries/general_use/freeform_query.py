#/usr/bin/python

import mx.ODBC.unixODBC as odbc
import numpy as np
import sys

# Connect to the database
db = odbc.DriverConnect("DSN=ramses17;UID=wsaro;PWD=wsaropw")

# Initiate the Cursor
cursor = db.cursor()

sql_cmd = sys.argv[1]

# Execute the Query
cursor.execute('SELECT COUNT(*)		\
FROM BestDR8..galaxy as g 			\
JOIN BestDR8..specObj as s			\
ON s.specObjID= g.specObjID 		\
WHERE s.primTarget=0x00000040	')

# Get the results
rows = cursor.fetchall()

print(rows)

# save results in numpy array
#np.save(sys.argv[2],rows)

# Close the database connection
db.close()

