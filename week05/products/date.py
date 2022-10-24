
from datetime import datetime, timedelta

current_date_and_time = datetime.now()
current_date_and_time.weekday()
print(f"{current_date_and_time}")

today = datetime.now()
one_day = timedelta(days=1)
yesterday = today - one_day
""" print(today.day)
print(today.month)
print(today.year) """
