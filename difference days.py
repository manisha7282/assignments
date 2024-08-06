
from datetime import datetime
def no_of_days(date1,date2):

    date_format = "%d-%m-%y"
    try:
        a=datetime.strptime(date1,date_format)
        b=datetime.strptime(date2,date_format)
        diff = b-a
        return abs(diff.days)
    except ValueError:
        return "Incorrect date format"
date1=input("enter the first date:")
date2=input("enter the first date:")

days=no_of_days(date1,date2)
print(f"the number of days between {date1} and {date2} is:{days}")

