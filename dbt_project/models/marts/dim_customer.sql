select customer_id, customer_name, segment, region from {{ ref('stg_customers') }}
