import pandas as pd

def solution(products: pd.DataFrame, order_items: pd.DataFrame) -> pd.DataFrame:
    # Write your solution here
    df = pd.merge(products, order_items, how='left', left_on ='id', right_on ='product_id')
    df1 = df[df['product_id'].isna()][['name','price']].sort_values(by='name')
    return df1