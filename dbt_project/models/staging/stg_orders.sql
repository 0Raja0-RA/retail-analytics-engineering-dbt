select order_id, customer_id, product_id, cast(order_date as date) as order_date, quantity, unit_price from {{ source('raw', 'orders') }}
