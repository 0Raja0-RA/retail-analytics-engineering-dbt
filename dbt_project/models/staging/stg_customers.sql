select customer_id, customer_name, segment, region from {{ source('raw', 'customers') }}
