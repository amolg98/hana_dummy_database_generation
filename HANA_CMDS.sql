#CREATE TABLE  "ORDERS" ( "ORD_NUM" INTEGER(6,0) NOT NULL PRIMARY KEY, "ORD_AMOUNT" INTEGER(12,2) NOT NULL, "ADVANCE_AMOUNT" INTEGER(12,2) NOT NULL, "ORD_DATE" DATE NOT NULL, "CUST_CODE" VARCHAR2(6) NOT NULL REFERENCES CUSTOMER,"AGENT_CODE" CHAR(6) NOT NULL REFERENCES AGENTS, "ORD_DESCRIPTION" VARCHAR2(60) NOT NULL);

# CREATE COLUMN TABLE "ORDERS" ( "ORDER_ID" VARCHAR(40) NOT NULL PRIMARY KEY, "ORD_AMOUNT" INTEGER(12,2) NOT NULL, "ADVANCE_AMOUNT" INTEGER(12,2) NOT NULL, "ORD_DATE" DATE NOT NULL, "CUST_CODE" VARCHAR2(6) NOT NULL REFERENCES CUSTOMER,"AGENT_CODE" CHAR(6) NOT NULL REFERENCES AGENTS, "ORD_DESCRIPTION" VARCHAR2(60) NOT NULL);

# Find description of table structure
SELECT COLUMN_NAME, POSITION FROM SYS.COLUMNS WHERE SCHEMA_NAME = 'YOUR_SCHEMA' AND TABLE_NAME = 'VBAK';
SELECT COLUMN_NAME, DATA_TYPE_NAME, LENGTH, POSITION FROM SYS.COLUMNS WHERE TABLE_NAME = 'CUSTOMERS';

========================================================================================================
# Create Customers table
CREATE COLUMN TABLE "CUSTOMERS" ( "CUST_ID" VARCHAR(40) NOT NULL PRIMARY KEY, "FIRST_NAME" VARCHAR(20), "LAST_NAME" VARCHAR(20), "PHONE_NUMBER" VARCHAR(10))

# Create Agents table
CREATE COLUMN TABLE "WORKERS" ("WORKER_ID" VARCHAR(40) NOT NULL PRIMARY KEY, "WORKER_NAME" VARCHAR(40), "WORKING_AREA" VARCHAR(35), "COMMISSION" DECIMAL(10,2), "PHONE_NUM" VARCHAR(10), "COUNTRY" VARCHAR(30))

# Create Orders table
CREATE COLUMN TABLE "ORDERS" ( "ORDER_ID" VARCHAR(2000) NOT NULL PRIMARY KEY, "ORDER_AMOUNT" DECIMAL(20,2) NOT NULL, "ADVANCE_AMOUNT" DECIMAL(20,2) NOT NULL, "ORDER_DATE" DATE NOT NULL, "CUST_ID" VARCHAR2(1000) NOT NULL REFERENCES CUSTOMERS,"WORKER_ID" VARCHAR(1000) NOT NULL REFERENCES WORKERS, "ORDER_DESC" VARCHAR2(3000) NOT NULL);

# Create pictures table
CREATE COLUMN TABLE "PICTURES" ("PIC_ID" VARCHAR(2000) NOT NULL PRIMARY KEY, "PIC_DETAILS" BLOB NOT NULL)
========================================================================================================