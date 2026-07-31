import pandas as pd

def solution(employees: pd.DataFrame) -> pd.DataFrame:
    df = employees.groupby('department', as_index=False).agg(min_age=('age','min'))
    df.sort_values('department',inplace=True)
    return df