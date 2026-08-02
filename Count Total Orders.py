import pandas as pd

def solution(orders: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame({
        "total_orders":[orders['order_id'].count()]
    })