#/usr/bin/python

import mx.ODBC.unixODBC as odbc
import pandas as pd
import numpy as np

# Connect to the database
db = odbc.DriverConnect("DSN=ramses17;UID=wsaro;PWD=wsaropw")

# Initiate the Cursor
cursor = db.cursor()

# just gets ra and dec for every value in each of the tables

# Execute the Query
sql_string = 'SELECT s.ra, s.dec FROM BestDR13..photoObjAll as s; ' 
	
cursor.execute(sql_string)

print('Cursor executed')

df = pd.DataFrame([], columns=['RA','DEC'])

rows = []
# Get the results
for row in cursor:
    	df2 = pd.DataFrame([[row[0],row[1]]], columns=['RA','DEC'])
    	df = df.append(df2)

print('SDSS results fetched',df.shape)

# save results in csv
df.to_csv('sdss_catalog.txt')

# Close the database connection
db.close()
