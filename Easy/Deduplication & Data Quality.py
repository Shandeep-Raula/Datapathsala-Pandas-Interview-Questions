data = (raw_orders.sort_values('created_at', ascending=False)
          .drop_duplicates('order_id')
          .sort_values('order_id'))
result = data[['order_id', 'customer_email', 'amount', 'status', 'created_at']]
result