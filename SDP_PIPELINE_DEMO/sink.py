from pyspark import pipelines as dp
from pyspark.sql import functions as F


dp.create_sink(
    name="local_silver_orders_sink",
    format="delta",
    options={"tableName": "sdp_utube_demo.silver.sink_orders"}
)


@dp.append_flow(
    target="local_silver_orders_sink",
    name="flow_to_delta_sink"
)
def stream_to_local_delta():
    # Reading from the bronze customers table
    customers_stream = spark.readStream.table("sdp_utube_demo.bronze.cdc_raw_customers")
    
    return (
        customers_stream.filter(F.col("CustomerID").isNotNull())
        .select(
            F.col("CustomerID").alias("customer_id"),
            F.col("Age").cast("integer").alias("age")
        )
    )