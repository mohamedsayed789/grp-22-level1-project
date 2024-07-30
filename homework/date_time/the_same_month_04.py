#Check if all dates in a list are in the same month
from datetime import datetime
from dateutil.relativedelta import relativedelta
#Input
dates_list = [
    datetime(2023, 12, 31),
    datetime(2023, 12, 15),
    datetime(2023, 12, 15),
    datetime(2023, 12, 1)
]
M = dates_list[0].date().month
is_found = False
for i in dates_list:
    if i == M:
        print('dates are in the same month')
        is_found = True
if not is_found:
    print('dates not are in the same month')



