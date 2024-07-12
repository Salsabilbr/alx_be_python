from datetime import datetime, timedelta
def display_current_datetime():
    current_date = datetime.now()
    print("Current Date and Time:", current_date.strftime("%Y-%m-%d %H:%M:%S")
def calculate_future_date():
    days_to_add = int(input("Enter the number of days to add: "))
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days_to_add)
    print("Future Date:", future_date.strftime("%Y-%m-%d"))
display_current_datetime()
calculate_future_date()
