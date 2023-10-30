import numpy as np
import datetime as dt
from datetime import date

today = date.today()

start = dt.date( 2023, 8, 29 )

today_month = int(today.strftime('%m'))
today_day = int(today.strftime('%d'))
today_year = int(today.strftime('%Y'))

end = dt.date(today_year, today_month, today_day)

total_days = np.busday_count(start, end) - 3

remainder = total_days % 7
print(f"You are on day {remainder} of the schedule.")