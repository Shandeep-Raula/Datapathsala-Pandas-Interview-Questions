import pandas as pd

def solution(products: pd.DataFrame) -> pd.DataFrame:
    # Write your solution here
    df = products.groupby('category', as_index=False).agg(product_count=('id','count')).sort_values(by=['product_count','category'],ascending=[False,True])
    return df
