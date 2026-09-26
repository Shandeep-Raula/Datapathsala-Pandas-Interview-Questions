import pandas as pd

def solution(employees: pd.DataFrame) -> pd.DataFrame:
    # Write your solution here
    employees['upper_name'] = employees['name'].str.upper()
    return employees[['upper_name','department']].sort_values(by=['department','upper_name'], ascending=[True,True])
