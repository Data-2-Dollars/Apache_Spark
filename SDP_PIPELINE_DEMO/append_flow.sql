-- Append flow is a construct used to incrementally ingest or transform data by adding new records from source to target (append), limited to Streaming tables


---1.) Declare the main target table (excatly once)
CREATE OR REFRESH  STREAMING TABLE GOLD_UNIFIED_TABLE
COMMENT "Consolated table for all the data from mutliple streams";


---2.) Attach the first streaming source {flow}

CREATE FLOW append_from_silver_sql
as INSERT INTO GOLD_UNIFIED_TABLE BY NAME
SELECT order_id from STREAM(stream_silver_cust_orders_py);


---2.) Attach the first streaming source {flow}

CREATE FLOW append_from_silver_py
as INSERT INTO GOLD_UNIFIED_TABLE BY NAME
SELECT order_id from STREAM(silver_cust_orders_stream);


/*CREATE FLOW append_from_silver_py_maat
as INSERT INTO GOLD_UNIFIED_TABLE BY NAME
SELECT order_id from STREAM(silver_cust_orders_py);*/








