import pandas as pd

def solution(customers: pd.DataFrame) -> pd.DataFrame:
    customers['full_address'] = (customers[['street','city','state','zip_code']].astype(str).agg(', '.join, axis=1))
    return (customers[['customer_id','full_address']].sort_values('customer_id').reset_index(drop=True))