import pandas as pd

def solution(order_items: pd.DataFrame) -> pd.DataFrame:
    # Write your solution here
    order_items['total'] = order_items['quantity'] * order_items['unit_price']
    df = order_items.groupby('product_name', as_index=False).agg(total_revenue=('total','sum')).sort_values(by='total_revenue', ascending=False)
    return df
