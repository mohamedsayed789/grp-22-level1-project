# program to count fridays, or saturday in a specific month
from datetime import datetime
from dateutil.relativedelta import relativedelta

#inputs
the_year = 2024
the_month = 7

#processing
custom_date = datetime(year=the_year, month=the_month, day=1) # 1-7-2024
end_date = custom_date + relativedelta(months=1) # 1-8-2024

weekend_counter = 0
while custom_date < end_date:
    if custom_date.date().weekday() in [4, 5]: # friday = 4, saturday = 5
        weekend_counter += 1
    custom_date = custom_date + relativedelta(days=1)

print('weekend counter = ', weekend_counter)

