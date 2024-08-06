import calendar
def no_of_weeks(year,month):
    month_calendar = calendar.monthcalendar(year,month)
    weeks = len(month_calendar)
    return weeks
year = int(input("enter the year:"))
month=int(input("enter the month:"))
weeks = no_of_weeks(year,month)
print(f"number of weeks in {calendar.month_name[month]} {year}: {weeks}")

     

    
     
