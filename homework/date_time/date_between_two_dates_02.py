#program checks if a specific date falls between two provided dates
from datetime import datetime
from dateutil.relativedelta import relativedelta
#Input
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)
given_date = datetime(2023, 6, 15)

is_found = False

for item in start_date, end_date:
    if given_date > start_date or given_date < end_date:
        print('given date falls between two dates')
        is_found = True
        break
if not is_found:
    print('given date not falls between two dates')





