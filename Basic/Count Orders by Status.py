import pandas as pd

def solution(orders: pd.DataFrame) -> pd.DataFrame:
    result = (
        orders.groupby("status")
        .size()
        .reset_index(name="order_count")
        .sort_values("status")
        .reset_index(drop=True)
    )

    return result