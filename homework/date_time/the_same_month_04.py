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


