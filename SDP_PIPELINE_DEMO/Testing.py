# Databricks notebook source
# MAGIC %sql
# MAGIC Select * from sdp_utube_demo.silver.silver_cust_orders;

# COMMAND ----------

# MAGIC %sql
# MAGIC Select * from sdp_utube_demo.silver.silver_cust_orders_py

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Mock Data for main.bronze.customers
# MAGIC INSERT INTO sdp_utube_demo.bronze.raw_customers (CustomerID, Gender, Age)
# MAGIC VALUES 
# MAGIC     (1, 'Female', 34),
# MAGIC     (2, 'Female', 28),
# MAGIC     (3, 'Male', 42),
# MAGIC     (4, 'Male', 31),
# MAGIC     (5, 'Female', 25);

# COMMAND ----------

# MAGIC %sql
# MAGIC Select * from sdp_utube_demo.bronze.raw_orders

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Mock Data for main.bronze.orders
# MAGIC INSERT INTO sdp_utube_demo.bronze.raw_orders (`Order ID`, `Product Category`, `Product Sub-Category`, `Product Name`, `Customer Name`,`Sales`)
# MAGIC VALUES 
# MAGIC     (-20, 'Office Supplies', 'Labels', 'Avery 49', 'Janice Fletcher',-200.45)
# MAGIC     -- ,
# MAGIC     -- (null, 'Office Supplies', 'Pens & Art Supplies', 'SANFORD Liquid Accent Highlighters', 'Bonnie Potter'),
# MAGIC     -- (null, 'Technology', 'Telephones and Communication', 'V70 Smartphone', 'Bonnie Potter')
# MAGIC     
# MAGIC     /*,
# MAGIC     (90193, 'Furniture', 'Chairs & Chairmats', 'Global Troy Executive Leather Chair', 'Ronnie Proctor'),
# MAGIC     (90194, 'Office Supplies', 'Appliances', 'Kensington 6 Outlet Power Control Center', 'Dwight Hwang');*/

# COMMAND ----------

# MAGIC %sql
# MAGIC Select * from sdp_utube_demo.silver.silver_cust_orders_stream

# COMMAND ----------

# MAGIC %sql
# MAGIC Select * from sdp_utube_demo.silver.stream_silver_cust_orders_py

# COMMAND ----------

# MAGIC %sql
# MAGIC Select * from sdp_utube_demo.gold.gold_cust_orders_py

# COMMAND ----------

# MAGIC %sql
# MAGIC Select * from sdp_utube_demo.gold.gold_table_python;

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE sdp_utube_demo.bronze.cdc_raw_customers (
# MAGIC     CustomerID INT,
# MAGIC     CustomerName STRING,
# MAGIC     City STRING,
# MAGIC     Age INT,
# MAGIC     LastUpdated TIMESTAMP
# MAGIC );
# MAGIC
# MAGIC INSERT INTO sdp_utube_demo.bronze.cdc_raw_customers VALUES 
# MAGIC (101, 'Jaswinder Singh', 'Amritsar', 25, '2026-06-27 09:00:00'),
# MAGIC (102, 'Bonnie Potter', 'Anacortes', 28, '2026-06-27 09:00:00');

# COMMAND ----------

# MAGIC %sql
# MAGIC Select * from sdp_utube_demo.silver.silver_cust_scd2_py

# COMMAND ----------

# MAGIC %sql
# MAGIC INSERT INTO sdp_utube_demo.bronze.cdc_raw_customers VALUES 
# MAGIC -- Update for existing customer (SCD1 will overwrite, SCD2 will version)
# MAGIC (101, 'Jaswinder Singh', 'Pune', 25, '2026-06-27 15:00:00'),
# MAGIC
# MAGIC -- Brand new customer (Both tables will insert a new row)
# MAGIC (103, 'Dwight Hwang', 'San Jose', 31, '2026-06-27 15:00:00');

# COMMAND ----------

# MAGIC %sql
# MAGIC Select * from sdp_utube_demo.silver.silver_customers_scd2

# COMMAND ----------

# MAGIC %sql
# MAGIC Select * from sdp_utube_demo.silver.sink_orders;