# program to go to specific day in a date
import calendar
from datetime import datetime
from dateutil.relativedelta import relativedelta

today = datetime.now() # 13-7-2024
print(today)
print('---go to the first day in this month---')#1-7-2024
first_date = today + relativedelta(day=1) #1-7-2024
print('frist day = ', first_date)

print('---go to the last day in this month----')# 31-7-2024
last_date = today + relativedelta(day=31) # 31-7-2024
print('last day = ', last_date)

#problem:
print('----go to the last day in the next month----')#31-8-2024
next_month_last_date = today + relativedelta(months=1, day=31)
print('next month last day = ', next_month_last_date)

print('---the nearest sunday from today---')
nearset_sunday = today + relativedelta(weekday=calendar.SUNDAY)
print('nearset day = ', nearset_sunday)

print('---the nearest 2nd sunday from today---')
nearest_2nd_sunday = today + relativedelta(weekday=calendar.SUNDAY, weeks=1)
print('the nearest 2nd sunday from today = ', nearest_2nd_sunday)
