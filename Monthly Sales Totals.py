import pandas as pd

def solution(sales: pd.DataFrame) -> pd.DataFrame:
    # Write your solution here
    sales['month_year'] = sales['sale_date'].dt.strftime('%Y-%m')
    df = sales.groupby('month_year',as_index=False).agg(total_amount=('amount','sum')).sort_values(by='month_year',ascending=True)
    return df