select product_id, product_name, category_id, category_name, department, unit_price from {{ source('raw', 'products') }}
