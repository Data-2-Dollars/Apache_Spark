/*--1 Decalre the Streaming table

CREATE OR REFRESH STREAMING TABLE silver_customer_scd1
Comment "Implementing SCD Type1";

CREATE OR REFRESH STREAMING TABLE silver_customer_scd2
Comment "Implementing SCD Type2";

-- @ Apply CDC for SCD Type 1 (Upsert)
APPLY CHANGES INTO silver_customer_scd1
FROM STREAM(sdp_utube_demo.bronze.cdc_raw_customers)
KEYS (CustomerID)
SEQUENCE BY LastUpdated
STORED AS SCD TYPE 1;


-- @ Apply CDC for SCD Type 2 (hISTORICAL)
APPLY CHANGES INTO silver_customer_scd2
FROM STREAM(sdp_utube_demo.bronze.cdc_raw_customers)
KEYS (CustomerID)
SEQUENCE BY LastUpdated
STORED AS SCD TYPE 2;*/