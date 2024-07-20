#Find the earliest (oldest) date from a list of dates 1
from datetime import datetime
from dateutil.relativedelta import relativedelta
#Input
dates_list = [datetime(2023, 12, 31), datetime(2023, 8, 15), datetime(2023, 5, 1)]
older_date = dates_list[0]
for item in dates_list:
    if item < older_date:
        older_date = item
print('older date = ', older_date.date())
#Check if a specific date exists in a list of dates 2
#inputs
given_date = datetime(2023, 8, 15)
dates_list = [datetime(2023, 12, 31), datetime(2023, 8, 15), datetime(2023, 5, 1)]
is_found = False

for i in range(len(dates_list)):
    if given_date == dates_list[i]:
        print('given date is found at index = ', i)
        is_found = True
        break

if not is_found:
    print('given date is not found')




