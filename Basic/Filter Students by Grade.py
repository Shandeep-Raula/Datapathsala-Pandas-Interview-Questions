import pandas as pd

def solution(students: pd.DataFrame) -> pd.DataFrame:
    # Write your solution here
    df = students.query('grade >= 85')[['name','grade']].sort_values(by=['grade','name'], ascending=[False, True])
    return df