/****** Object:  Table dbo.Geography_Dim    Script Date: 13/09/2021 16:50:00 ******/
DROP TABLE if exists Geography_Dim;


CREATE TABLE Geography_Dim(
	Street_ID int NOT NULL,
	Continent nvarchar(30) NULL,
	Country nvarchar(2) NULL,
	State_Code nvarchar(2) NULL,
	_State nvarchar(25) NULL,
	Region nvarchar(30) NULL,
	Province nvarchar(30) NULL,
	County nvarchar(60) NULL,
	City nvarchar(30) NULL,
	Postal_Code nvarchar(10) NULL,
	Street_Name nvarchar(45) NULL
); 


