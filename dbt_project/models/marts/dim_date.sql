select distinct order_date as full_date, extract(year from order_date) as year, extract(month from order_date) as month, extract(quarter from order_date) as quarter from {{ ref('stg_orders') }}
