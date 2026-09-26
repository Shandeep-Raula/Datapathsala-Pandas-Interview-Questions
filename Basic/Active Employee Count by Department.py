import pandas as pd

def solution(employees: pd.DataFrame) -> pd.DataFrame:
    # Write your solution here
    df = employees[employees["status"] == "active"].groupby(by='department',as_index=False).agg(active_count=('id','count')).sort_values(by=['active_count','department'],ascending=[False,True])
    return df.head(3)