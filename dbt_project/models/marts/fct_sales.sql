select order_id, order_date, customer_id, product_id, quantity, unit_price, sales_amount from {{ ref('int_sales') }}
