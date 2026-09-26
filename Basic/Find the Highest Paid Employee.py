import pandas as pd

def solution(employees: pd.DataFrame) -> pd.DataFrame:
    # Write your solution here
    df = employees[['name','salary']].sort_values(by=['salary','name'], ascending=[False,True])
    return df.head(1)