-- -- Expectations are how u implement the data quality constraints within ur data pipilines
-- --Retain(Warn)   --- Drop    --- Fail 

-- CREATE OR REFRESH STREAMING TABLE exp_silver_orders_validated
-- (
--     --CONSTRAINT valid_order_id EXPECT (order_id is not null)  ---Retian behaviour

--   -- CONSTRAINT positive_sales EXPECT (sales_amount > 0) ON VIOLATION DROP ROW  --Drop Bbehaviour

--     CONSTRAINT critical_id_check EXPECT (order_id > 0) ON VIOLATION FAIL UPDATE  --fAIL bEHAVIOUR

-- )
-- AS
-- SELECT `Order ID` as order_id,
-- CAST(`Sales` as Double) as sales_amount
-- from STREAM(sdp_utube_demo.bronze.raw_orders);
