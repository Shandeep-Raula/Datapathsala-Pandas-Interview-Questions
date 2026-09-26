import pandas as pd

def solution(daily_sales: pd.DataFrame) -> pd.DataFrame:
    # Write your solution here
    daily_sales['date_id'] = pd.to_datetime(daily_sales['date_id']).dt.strftime('%Y-%m-%d')
    df = daily_sales.groupby(['date_id','make_name'], as_index=False).agg(unique_leads=('lead_id','nunique'),unique_partners=('partner_id', 'nunique'))
    return df
