import pandas as pd

def solution(employees: pd.DataFrame) -> pd.DataFrame:
    # Write your solution here
    return employees[['name','salary','department']].sort_values(by=['salary','name'], ascending=[False,True])