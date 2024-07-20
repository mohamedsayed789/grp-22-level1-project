#Count occurrences of a specific date in a list
from datetime import datetime
from dateutil.relativedelta import relativedelta

#Input
dates_list = [
    datetime(2023, 12, 31),
    datetime(2023, 8, 15),
    datetime(2023, 8, 15),
    datetime(2023, 5, 1)
]
given_date = datetime(2023, 8, 15)
count_occur = 0
for item in dates_list:
    if given_date == item:
        count_occur = count_occur + 1

print(given_date.date(),'Count occurrences = ', count_occur)