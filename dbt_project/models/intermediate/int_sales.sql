select order_id, order_date, customer_id, product_id, quantity, unit_price, quantity * unit_price as sales_amount from {{ ref('stg_orders') }}
