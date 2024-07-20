# program to get the difference between 2 dates
from datetime import datetime #from module datetime import class datetime

#from relativedelta module found in deateutil pkg import relativedelta class
from dateutil.relativedelta import relativedelta

today = datetime.now()
custom_date = datetime(year=2024, month=4, day=17)
print('today = ', today)
print('custom date = ', custom_date)

difference_in_days = today - custom_date
print(difference_in_days)
print(difference_in_days.days)

print('-------------')
difference_parts = relativedelta(today, custom_date)
print(difference_parts)
print('differ in years = ', difference_parts.years)
print('differ in months = ', difference_parts.months)
print('differ in day = ', difference_parts.days)

