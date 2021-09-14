USE dwh_orion;

/****** Object:  Table dbo.Customer_Dim    Script Date: 10/11/2018 17:48:08 ******/
DROP TABLE if exists Customer_Dim;


CREATE TABLE Customer_Dim(
	Customer_ID int NULL,
	Customer_Country nvarchar(2) NULL,
	Customer_Group nvarchar(40) NULL,
	Customer_Type nvarchar(40) NULL,
	Customer_Gender nvarchar(1) NULL,
	Customer_Age_Group nvarchar(12) NULL,
	Customer_Age smallint NULL,
	Customer_Name nvarchar(40) NULL,
	Customer_Fisrtname nvarchar(20) NULL,
	Customer_Lastname nvarchar(30) NULL,
	Customer_Birth_Date date NULL
) 


