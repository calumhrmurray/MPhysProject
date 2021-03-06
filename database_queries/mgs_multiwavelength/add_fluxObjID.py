#/usr/bin/python

import mx.ODBC.unixODBC as odbc
import numpy as np

# Connect to the database
db = odbc.DriverConnect("DSN=ramses17;UID=wsaro;PWD=wsaropw")

# Initiate the Cursor
cursor = db.cursor()

# Add lasID column to the table
# Execute the Query
cursor.execute("ALTER TABLE cmurray..mgs_multiwavelength ADD objID bigint;") 

# Add lasIDs into the table
# query for lasID
cursor.execute("					\
UPDATE cmurray..mgs_multiwavelength 			\
SET cmurray..mgs_multiwavelength.objID = s.fluxObjID	\
	FROM cmurray..mgs_multiwavelength as m 		\
 	INNER JOIN BestDR13..specObj as s		\
 	on s.specObjID = m.specObjID  ")
 
# show table
cursor.execute("SELECT COUNT(objID) 		\
		FROM cmurray..mgs_multiwavelength	\
		WHERE objID != 0")

# Get the results
rows = cursor.fetchall()

print(rows)

# show table
cursor.execute("SELECT COUNT(*) 		\
		FROM cmurray..mgs_multiwavelength")

# Get the results
rows = cursor.fetchall()

print(rows)

# Commit the change
db.commit()
# Close the database connection
db.close()
