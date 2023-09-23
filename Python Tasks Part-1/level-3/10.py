from datetime import datetime

def calc_countdown(date1, date2):
    try:
        date1 = datetime.strptime(date1, '%Y-%m-%d')
        date2 = datetime.strptime(date2, '%Y-%m-%d')

        time_diff = abs(date2-date1)
    except ValueError:
        print("Invalid date format")
    else:
        time_diff_days = int(time_diff.days)
        year = time_diff_days//365
        time_diff_days = time_diff_days - (year*365)
        month = time_diff_days//30
        day = time_diff_days%30
        return (year, month, day)


d1 = input("Enter first date: (Year-Month-Day): ")
d2 = input("Enter second date: (Year-Month-Day): ")

result = calc_countdown(d1, d2)

if result:
    print(f"Time between the {d1} and {d2} is: {result[0]} years, {result[1]} months, and {result[2]} daysd.")


