import datetime
def display_current_datetime():
    current_date = datetime.datetime.now()
    formatted_date = current_date("%Y-%m-%d %H:%M:%S")
    print("Current Date and Time:", formatted_date)
    display_current_datetime()
def calculate_future_date():
    current_date = datetime.date.today()
    num_days = int(input("Enter the number of days: "))
    future_date = current_date + datetime.timedelta(days=num_days)
    print("Future Date:", future_date.strftime("%Y-%m-%d"))
    calculate_future_date()
