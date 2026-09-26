import pandas as pd

def solution(contacts: pd.DataFrame) -> pd.DataFrame:
    # Write your solution here
    df = contacts.groupby('phone_number',as_index=False).agg(count_occurrences=('phone_number','count')).sort_values(by=['count_occurrences','phone_number'],ascending=[False,True])
    return df.query('count_occurrences >= 2 ')
