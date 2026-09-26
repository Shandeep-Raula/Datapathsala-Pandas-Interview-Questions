import pandas as pd

def solution(products: pd.DataFrame) -> pd.DataFrame:
    # Write your solution here
    products['discounted_price'] = (products['original_price'] * (1 - products['discount_percent']/100)).round(2)

    df = products[['name','original_price','discounted_price']].sort_values(by='discounted_price', ascending=True)
    return df