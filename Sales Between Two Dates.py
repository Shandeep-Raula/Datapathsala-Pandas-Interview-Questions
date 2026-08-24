import pandas as pd

def solution(sales: pd.DataFrame) -> pd.DataFrame:
    # Write your solution here
    df = sales[sales['sale_date'].between('2024-01-01','2024-03-31')].sort_values(by='sale_date', ascending=True)
    return df[['salesperson','amount']]