import pandas as pd

def solution(employees: pd.DataFrame) -> pd.DataFrame:
    # Write your solution here
    employees['annual_salary'] = employees['monthly_salary'] * 12
    df = employees[['name','monthly_salary','annual_salary']].sort_values(by='annual_salary', ascending=False)
    return df
