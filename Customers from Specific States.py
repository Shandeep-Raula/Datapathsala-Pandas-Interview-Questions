import pandas as pd

def solution(customers: pd.DataFrame) -> pd.DataFrame:
    # Write your solution here
    df = customers[customers['state'].isin(['CA','NY','TX'])][['name','state']].sort_values(by=['state','name'], ascending=[True,True])
    return df