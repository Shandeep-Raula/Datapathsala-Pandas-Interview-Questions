import pandas as pd

def solution(orders: pd.DataFrame, customers: pd.DataFrame) -> pd.DataFrame:
    # Write your solution here
    df = pd.merge(orders, customers, how='inner', left_on='customer_id', right_on='id')[['name','amount']].sort_values(by='amount', ascending=False)
    return df
