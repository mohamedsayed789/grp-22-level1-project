#Create a list of dates within a date range included
from datetime import datetime
from dateutil.relativedelta import relativedelta

#Input
start_range = datetime(2023, 1, 1)
end_range = datetime(2023, 1, 10)
list_dates = []
for item in start_range, end_range:
    if start_range < end_range:
        list_dates.append(item.date())

print(list_dates)




