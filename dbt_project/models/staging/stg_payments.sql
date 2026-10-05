select payment_id, order_id, payment_amount, payment_method, payment_status from {{ source('raw', 'payments') }}
