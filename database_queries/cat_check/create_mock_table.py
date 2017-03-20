#/usr/bin/python

# Sample script for connecting to SDSS DR9, running a query, and printing results

import mx.ODBC.unixODBC as odbc
import numpy as np

# Connect to the database
db = odbc.DriverConnect("DSN=ramses17;Database=cmurray;UID=wsaro;PWD=wsaropw")

# Initiate the Cursor
cursor = db.cursor()

# Execute the Query
cursor.execute("CREATE TABLE mock_las			\
			(					\
			mobjID bigint,				\
			sobjID bigint,				\
			distance real);") 
# load dataset
cursor.execute("INSERT INTO mock_las (mobjID, sobjID, distance) \
			VALUES 							\
			(1, 5, 0.23),						\
			(2, 5, 0.02),						\
			(2, 4, 1.01),						\
			(3, 3, 0.21),						\
			(4, 5, 2.46),						\
			(4, 3, 0.30),						\
			(4, 1, 0.79),						\
			(5, 1, 0.51),						\
			(5, 2, 0.10),						\
			(6, 2, 2.23);")

# Execute the Query
cursor.execute("CREATE TABLE mock_mgs			\
			(objID bigint);") 
# load dataset
cursor.execute("INSERT INTO mock_mgs (objID) \
			VALUES 							\
			(1),						\
			(2),						\
			(3),						\
			(4),						\
			(5);")

# Execute the Query
cursor.execute("SELECT * FROM mock_las as out				\
		JOIN mock_mgs ON objID = sobjID				\
		WHERE distance IN (					\
			SELECT MIN(distance)			\
				FROM mock_las as m			\
				WHERE m.mobjID = out.mobjID)")

# Get the results
rows = cursor.fetchall()

for row in rows:
	print(row)

print('New query')

# Execute the Query
cursor.execute("SELECT * FROM mock_las as out				\
		JOIN mock_mgs ON objID = sobjID				\
		WHERE distance IN (					\
			SELECT MIN(distance)			\
				FROM mock_las as m			\
				WHERE m.mobjID = out.mobjID)		\
		AND distance IN (					\
			SELECT MIN(distance)			\
				FROM mock_las			\
				WHERE sobjID = mock_mgs.objID)")

# Get the results
rows = cursor.fetchall()

for row in rows:
	print(row)

print('New query')

# Execute the Query
cursor.execute("SELECT * FROM mock_las as out				\
		JOIN mock_mgs ON objID = sobjID				\
		WHERE distance IN (					\
			SELECT MIN(distance)			\
				FROM mock_las as m			\
				WHERE m.mobjID = out.mobjID)		\
		AND distance IN (					\
			SELECT MIN(distance)			\
				FROM mock_las			\
				WHERE sobjID = out.sobjID)")

# Get the results
rows = cursor.fetchall()

for row in rows:
	print(row)

# Commit the change
#db.commit()
# Close the database connection
db.close()
