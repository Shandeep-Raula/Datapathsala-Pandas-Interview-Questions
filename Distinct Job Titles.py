import pandas as pd

def solution(employees: pd.DataFrame) -> pd.DataFrame:
    df = employees[["job_title"]].drop_duplicates().sort_values("job_title").reset_index(drop=True)
    return df