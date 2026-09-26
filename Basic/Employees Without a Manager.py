import pandas as pd

def solution(employees: pd.DataFrame) -> pd.DataFrame:
    df = employees[employees['manager_id'].isna()]
    return df[['name', 'department']]