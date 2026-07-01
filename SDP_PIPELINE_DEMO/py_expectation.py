# from pyspark import pipelines as dp
# from pyspark.sql import functions as F

# @dp.table(
#     name="exp_silver_orders_validated_py",
#     comment="Phtyhon Validations"
# )

# # @dp.expect_all({
# #     "valid_order_id": "order_id is not null",
# #     "reasonable_sales":"sales_amount <100000"
# # }
# # )


# # @dp.expect_all_or_drop({
# #     "positive_sales": "sales_amount >0"
# # })

# @dp.expect_or_fail(
#        "critical_id_chekcs","order_id >0" 
# )

# def exp_silver_orders_validated_py():
#     return (
#         spark.readStream.table("sdp_utube_demo.bronze.raw_orders")
#         .select(
#             F.col("`Order ID`").alias("order_id"),
#             F.col("`Product Name`").alias("product_name"),
#             F.col("`Sales`").alias("sales_amount")
#         )
#     )



