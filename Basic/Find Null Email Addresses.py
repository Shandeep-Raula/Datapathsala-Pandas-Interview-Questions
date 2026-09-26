import pandas as pd

def solution(users: pd.DataFrame) -> pd.DataFrame:
    df = users[users['email'].isnull()]
    return df[['user_id','username']]