/****** Object:  Table dbo.Organization    Script Date: 13/09/2021 16:45:00 ******/
DROP TABLE if exists Organization_Dim;


CREATE TABLE Organization_Dim(
	Employee_ID int NOT NULL,
    Employee_Country nvarchar(2) NULL,
    Company nvarchar(30) NULL,
    Department nvarchar(40) NULL,
    Section nvarchar(40) NULL,
    Org_Group nvarchar(40) NULL,
    Job_Title nvarchar(25) NULL,
    Employee_Name nvarchar(40) NULL,
    Employee_Gender nvarchar(1) NULL,
    Salary decimal(13) NULL,
    Employee_Birth_Date date NULL,
    Employee_Hire_Date date NULL,
    Employee_Term_Date date NULL
); 