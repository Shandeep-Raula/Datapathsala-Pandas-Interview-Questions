import pandas as pd

def solution(employees: pd.DataFrame) -> pd.DataFrame:
    # Write your solution here
    employees['full_name'] = employees['first_name'] + " " + employees['last_name']
    return employees[['full_name','department']].sort_values(by='full_name', ascending=True)