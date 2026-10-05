{{ config(materialized='incremental', unique_key='order_id') }}
select order_id, order_date, customer_id, product_id, quantity, unit_price, sales_amount from {{ ref('int_sales') }}
{% if is_incremental() %}
where order_date >= (select coalesce(max(order_date), cast('1900-01-01' as date)) from {{ this }})
{% endif %}
