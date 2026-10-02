daily_temperatures['prev_temp'] = daily_temperatures['temperature'].shift(1)
daily_temperatures['temp_change'] = daily_temperatures['temperature'] - daily_temperatures['prev_temp']
result = daily_temperatures[['record_date','temperature','prev_temp','temp_change']]
result