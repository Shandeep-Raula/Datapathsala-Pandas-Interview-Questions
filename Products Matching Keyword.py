import pandas as pd

def solution(products: pd.DataFrame) -> pd.DataFrame:
    # Write your solution here
    df = products[products['name'].str.contains('Pro')][['name','price']].sort_values(by='name', ascending=True)
    return df