import pandas as pd

def solution(employees: pd.DataFrame) -> pd.DataFrame:
    # Write your solution here
    df = employees.groupby('department', as_index=False).agg(employee_count=('id','count'))
    return df.query('employee_count >= 5').sort_values(by='employee_count', ascending=False)