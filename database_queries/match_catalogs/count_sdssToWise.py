SELECT COUNT(*)
FROM galaxy as g 
INNER JOIN wise_xmatch as wise
on wise.sdss_objid = g.objid
INNER JOIN specObj as s
on s.specObjID = g.specObjID
WHERE s.primTarget = 0x00000040 
AND match_dist IN (	
 	SELECT MIN(match_dist)		
	FROM wise_xmatch	
	WHERE sdss_objid = g.objid)
