/****** Object:  Table dbo.Time_Dim    Script Date: 13/09/2021 16:57:00 ******/
DROP TABLE if exists Time_Dim;


CREATE TABLE Time_Dim(
    Date_ID date NOT NULL,
    Year_ID nvarchar(4) NULL,
    Quarter nvarchar(6) NULL,
    Month_Name nvarchar(20) NULL,
    Weekday_Name nvarchar(20) NULL,
    Month_Num smallint NULL,
    Weekday_Num smallint NULL
);