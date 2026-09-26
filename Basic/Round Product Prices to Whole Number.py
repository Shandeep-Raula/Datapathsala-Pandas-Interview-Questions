import pandas as pd

def solution(products: pd.DataFrame) -> pd.DataFrame:
    # Write your solution here
    products['rounded_price'] = products['price'].round()
    return products[['name','rounded_price']].sort_values(by='rounded_price', ascending=True)
