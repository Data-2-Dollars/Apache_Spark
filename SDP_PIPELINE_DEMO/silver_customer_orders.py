from pyspark import pipelines as dp
from pyspark.sql import functions as F

@dp.materialized_view(
    name="silver_cust_orders_py",
    comment="Cleaned and joined customers & orders dataset"
)

def silver_cust_orders_py():
    orders_df = spark.read.table("bronze.raw_orders")
    cust_df = spark.read.table("bronze.raw_customers")

    return (
        orders_df.alias("o")
        .join(cust_df.alias("c"), F.col("o.`Customer ID`") == F.col("c.CustomerID"), "inner")
        .select(
            F.col("o.`Order ID`").alias("order_id"),
            F.col("o.`Product Category`").alias("product_category"),
            F.col("o.`Product Sub-Category`").alias("product_sub_category"),
            F.col("o.`Product Name`").alias("product_name"),
            F.col("o.`Customer Name`").alias("customer_name"),
            F.col("c.Gender").alias("gender"),
            F.col("c.Age").alias("age")
        )
    )
