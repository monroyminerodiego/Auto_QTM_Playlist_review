/*
Diego Monroy
2023-10-05
List of all 'IBO' companies that are:
	- Not suspendend
	- Not disabled
	- Inventory Only
	- Has non-retired faces

Pending:
	- Filter out faces that are out of sevice
*/


SELECT DISTINCT
	SellerID, 
	CompanyName
	--FaceID,
	--ClientFaceID,
	--ImageAS
	
FROM Company 
	INNER JOIN Face ON Face.SellerID = Company.CompanyID 
WHERE 1=1 
	AND AffiliatedTo = 'IBO' 
	AND Company.Suspended = 0 
	AND Company.Disabled = 0 
	AND Company.InventoryOnly = 1
	AND (RetirementDate IS NULL OR RetirementDate > getdate())
	-- AND (ImageAS IS NOT NULL AND  ImageAS != '')

ORDER BY SellerID