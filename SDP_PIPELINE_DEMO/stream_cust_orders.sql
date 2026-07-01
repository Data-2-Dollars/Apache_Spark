-- Materialized View

CREATE OR REFRESH STREAMING TABLE silver_cust_orders_stream
COMMENT "Cleaned and joined customers & orders dataset"
AS
SELECT
  o.`Row ID` AS row_id,
  o.`Order ID` AS order_id,
  o.`Order Date` AS order_date,
  o.`Order Priority` AS order_priority,
  o.Discount AS discount,
  o.`Unit Price` AS unit_price,
  o.`Shipping Cost` AS shipping_cost,
  o.`Customer ID` AS customer_id,
  o.`Customer Name` AS customer_name,
  o.`Ship Mode` AS ship_mode,
  o.`Customer Segment` AS customer_segment,
  o.`Product Category` AS product_category,
  o.`Product Sub-Category` AS product_sub_category,
  o.`Product Container` AS product_container,
  o.`Product Name` AS product_name,
  o.`Product Base Margin` AS product_base_margin,
  o.Region AS region,
  o.`State or Province` AS state_or_province,
  o.City AS city,
  o.`Postal Code` AS postal_code,
  o.`Ship Date` AS ship_date,
  o.Profit AS profit,
  o.`Quantity ordered new` AS quantity_ordered_new,
  o.Sales AS sales,
  c.Gender AS gender,
  c.Age AS age,
  c.`Annual Income (k$)` AS annual_income_k,
  c.`Spending Score (1-100)` AS spending_score
FROM STREAM(bronze.raw_orders) o
JOIN bronze.raw_customers c
ON o.`Customer ID` = c.CustomerID
