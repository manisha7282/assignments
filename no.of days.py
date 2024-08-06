from datetime import datetime, timedelta

def adding_dates(input_date, days):
    
    try:

        date_f = datetime.strptime(input_date, '%Y-%m-%d')
        delta = timedelta(days)
        new_date = date_f + delta
        new_date_f = new_date.strftime('%Y-%m-%d')
        return new_date_f
    except  ValueError:
        return "Invalid date format"

input_date = input("Enter a date : ")
days = int(input("Enter number  to add: "))

result_date = adding_dates(input_date, days)
print(f"The date after adding :{result_date}")
    

