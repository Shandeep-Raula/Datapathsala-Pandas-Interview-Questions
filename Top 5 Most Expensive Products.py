import pandas as pd

def solution(products: pd.DataFrame) -> pd.DataFrame:
    # Write your solution here
    df = products[['name','price']].sort_values(by='price', ascending=False)
    return df.head(5)