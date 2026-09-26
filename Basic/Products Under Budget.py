import pandas as pd

def solution(products: pd.DataFrame) -> pd.DataFrame:
    # Write your solution here
    df = products.query('price < 50')[['name','price']].sort_values(by='price', ascending=True)
    return df
