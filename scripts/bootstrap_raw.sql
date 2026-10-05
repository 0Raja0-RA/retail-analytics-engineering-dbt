-- Run this with DuckDB CLI or equivalent DuckDB client before dbt build.
CREATE SCHEMA IF NOT EXISTS raw;
CREATE OR REPLACE TABLE raw.customers AS SELECT * FROM read_csv_auto('../data/customers.csv', HEADER=TRUE);
CREATE OR REPLACE TABLE raw.products AS SELECT * FROM read_csv_auto('../data/products.csv', HEADER=TRUE);
CREATE OR REPLACE TABLE raw.orders AS SELECT * FROM read_csv_auto('../data/orders.csv', HEADER=TRUE);
CREATE OR REPLACE TABLE raw.payments AS SELECT * FROM read_csv_auto('../data/payments.csv', HEADER=TRUE);
