import pandas as pd

def solution(employees: pd.DataFrame) -> pd.DataFrame:
    # Write your solution here
    employees['hire_date'] = pd.to_datetime(employees['hire_date'])
    df = employees[employees['hire_date'].dt.year == 2024][['name','hire_date']].sort_values(by='hire_date', ascending=True)
    df['hire_date'] = df['hire_date'].dt.strftime('%Y-%m-%d')
    return df