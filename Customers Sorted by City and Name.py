import pandas as pd

def solution(customers: pd.DataFrame) -> pd.DataFrame:
    # Write your solution here
    df = customers[['name','city']].sort_values(by=['city','name'], ascending=[True, True])
    return df