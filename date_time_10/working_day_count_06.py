# program to get the date after 12 working days from a date
from datetime import datetime
from dateutil.relativedelta import relativedelta

today = datetime.now()
jump_working_days = 12

# start date = 13-7-2024             end_date = 29-7-2024

required_date = today
for i in range(jump_working_days):
    if required_date.date().weekday() == 3: # thursday         # لو احنا يوم الخميس هنزود ثلاثه ايام
        required_date = required_date + relativedelta(days=3)  # زود ثلاثه ايام
    elif required_date.date().weekday() == 4: # friday
        required_date = required_date + relativedelta(days=2)  # لو كان يوم الجمعه ازود يومين
    else:
        required_date = required_date + relativedelta(days=1)  # لو اى يوم غير الخميس والجمعه والسبت زود يوم واحد

print('the target date = ', required_date)




