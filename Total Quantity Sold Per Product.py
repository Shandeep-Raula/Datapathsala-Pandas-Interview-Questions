import pandas as pd

def solution(sales: pd.DataFrame) -> pd.DataFrame:
    df = sales.groupby('product_name', as_index=False).agg(total_quantity=('quantity','sum')).reset_index(drop=True)
    return df.sort_values(['total_quantity','product_name'],ascending=[False,True])