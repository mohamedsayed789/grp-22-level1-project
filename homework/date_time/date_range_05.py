#Create a list of dates within a date range included
from datetime import datetime
from dateutil.relativedelta import relativedelta

#Input
start_range = datetime(2023, 1, 1)
end_range = datetime(2023, 1, 10)
list_dates = []
date_range = 0
while start_range < end_range:
        date_range = date_range + relativedelta(days=1)
        list_dates.append(date_range)

print(date_range)