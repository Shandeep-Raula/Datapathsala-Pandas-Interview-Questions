import pandas as pd

def solution(customers: pd.DataFrame) -> pd.DataFrame:
    # Write your solution here
    df = customers[customers['email'].str.endswith('@gmail.com', na=False)]
    return df[['name','email']]