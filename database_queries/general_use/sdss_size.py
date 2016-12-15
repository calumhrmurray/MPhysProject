#/usr/bin/python

import mx.ODBC.unixODBC as odbc
import numpy as np

# Connect to the database
db = odbc.DriverConnect("DSN=ramses17;UID=wsaro;PWD=wsaropw")

# Initiate the Cursor
cursor = db.cursor()

# Execute the Query
sql_string = 'SELECT COUNT(*)		\
FROM BestDR13..galaxy as g 			\
JOIN BestDR13..specObj as s			\
ON s.specObjID= g.specObjID 		\
WHERE s.primTarget=0x00000040	' 
	
cursor.execute(sql_string)

print('Cursor executed')

# Get the results
rows = cursor.fetchall()

print(rows)

# Close the database connection
db.close()
