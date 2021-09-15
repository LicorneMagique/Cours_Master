/****** Object:  Table dbo.Order_Fact    Script Date: 13/09/2021 20:27:00 ******/
DROP TABLE if exists Order_Fact;


CREATE TABLE Order_Fact(
	Customer_ID int NULL REFERENCES Customer_Dim(Customer_ID),
    Employee_ID int NOT NULL REFERENCES Organization_Dim(Employee_ID),
    Street_ID int NOT NULL REFERENCES Geography_Dim(Street_ID),
    Product_ID bigint NOT NULL REFERENCES Product_Dim(Product_ID),
    Order_Date DATE NOT NULL REFERENCES Time_Dim(Date_ID),
    Order_Type smallint NULL,
    Delivery_Date date NULL,
    Quantity smallint NULL,
    Total_Retail_Price decimal(13,2) NULL,
    Costprice_Per_Unit decimal(13,2) NULL,
    Discount decimal(5,2) NULL
);
