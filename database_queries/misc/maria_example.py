import mx.ODBC.unixODBC as odbc

db = odbc.DriverConnect("DSN=ramses8;Database=BestDR9;UID=wsaro;PWD=wsaropw")

# Initiate the Cursor
cursor = db.cursor()

 # Execute the Query
sql_dr9="SELECT TOP 10 G.objID, G.ra, G.dec, F.dr7objid, P.z, P.zErr, P2.z, P2.zErr, G.dered_u, G.dered_g, G.dered_r, G.dered_i, G.dered_z  \
FROM  GALAXY as G JOIN Photoz as P on P.objID=G.objID \
JOIN PhotoObjDR7 as F on F.SpecObjID=G.specObjID \
JOIN PhotozRF as P2 on P2.objID=G.objID \
LEFT OUTER JOIN SpecObj as S on G.ObjID=S.bestObjID \
WHERE G.ra BETWEEN 120 AND 121 AND G.dec BETWEEN 30 AND 31 AND G.objID=P.objID AND (G.dered_i) < 21.0 AND (G.modelMagErr_g / G.dered_g) < 0.1 AND (G.modelMagErr_r / G.dered_r) < 0.1 "
    
cursor.execute(sql_dr9)
 # Get the results

data=cursor.fetchall()
print data

db.close()
