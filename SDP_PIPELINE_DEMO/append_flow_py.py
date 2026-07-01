from pyspark import pipelines as dp
from pyspark.sql import functions as F


#1 Create The unified Streaming Table
dp.create_streaming_table(name="gold_table_python")

# Append flow for Flow A
@dp.append_flow(target="gold_table_python",name='Flow_a')
def flow_a():
   return spark.readStream.table("silver_cust_orders_stream")


# Append flow for Flow B
@dp.append_flow(target="gold_table_python",name='Flow_b')
def flow_b():
   return spark.readStream.table("stream_silver_cust_orders_py")