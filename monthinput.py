# List of months and corresponding number of days (non-leap year)
while True:
    
    months = ["January", "February", "March", "April", "May", "June", 
            "July", "August", "September", "October", "November", "December"]

    days_in_month = [31, 28, 31, 30, 31, 30, 
                    31, 31, 30, 31, 30, 31]


    user_month = input("Enter the name of the month: ").capitalize() # User input

    # Check if month is valid
    if user_month in months:
        index = months.index(user_month)
        print(user_month + " " + str(days_in_month[index]) + " days.")
    else:
        print("Invalid month name.")
    break