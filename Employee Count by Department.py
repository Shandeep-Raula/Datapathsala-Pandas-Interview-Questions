import pandas as pd

def solution(employees: pd.DataFrame, departments: pd.DataFrame) -> pd.DataFrame:
    # Write your solution here
    df = pd.merge(departments, employees, how='left', left_on='id', right_on='dept_id')
    df1 = df.groupby('dept_name', as_index=False).agg(employee_count=('dept_id','count')).sort_values(by=['employee_count','dept_name'], ascending=[False,True])
    return df1
