import pandas as pd

def solution(reviews: pd.DataFrame) -> pd.DataFrame:
    # Write your solution here
    df = reviews.groupby('restaurant_name', as_index=False).agg(avg_rating=('rating','mean')).sort_values(by='avg_rating', ascending=False)
    return df