# from pyspark import pipelines as dp
# from pyspark.sql import functions as F

# # Creating Target Streaming tables for cdc
# dp.create_streaming_table(name="silver_cust_scd1_py")
# dp.create_streaming_table(name="silver_cust_scd2_py")


# #SCD Type-1

# dp.create_auto_cdc_flow(
#     target="silver_cust_scd1_py",
#     source="sdp_utube_demo.bronze.cdc_raw_customers",
#     keys=["CustomerID"],
#     sequence_by="LastUpdated",
#     stored_as_scd_type=1
# )


# #SCD Type-2

# dp.create_auto_cdc_flow(
#     target="silver_cust_scd2_py",
#     source="sdp_utube_demo.bronze.cdc_raw_customers",
#     keys=["CustomerID"],
#     sequence_by="LastUpdated",
#     stored_as_scd_type=2
# )