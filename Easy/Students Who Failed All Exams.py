import pandas as pd

def solution(students: pd.DataFrame, exams: pd.DataFrame) -> pd.DataFrame:
    # Write your solution here
    df = exams.groupby('student_id', as_index=False)['score'].max()
    df = df[df['score'] < 60]
    return students.merge(df, on='student_id')[['student_id', 'student_name']]