import pandas as pd

def solution(orders: pd.DataFrame) -> pd.DataFrame:
    # Write your solution here
    return (orders[['customer_name','amount']].query('amount > 500').sort_values(by='amount', ascending=False))