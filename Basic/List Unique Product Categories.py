import pandas as pd

def solution(products: pd.DataFrame) -> pd.DataFrame:
    # Write your solution here
    df = pd.DataFrame(products['category'].unique(), columns=['category'])
    return df.sort_values(by='category', ascending=True)