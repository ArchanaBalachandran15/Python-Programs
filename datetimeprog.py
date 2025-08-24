# Date time Program 

import datetime

# Get current date and time
x = datetime.datetime.now()
print(x)

# Uncomment to create a specific date
y = datetime.datetime(2025, 4, 15)
print(y)

# Convert string to datetime object using STRPTIME
date_string = "9/May/2025, 9:15"
date_object = datetime.datetime.strptime(date_string, "%d/%B/%Y, %H:%M")
print(date_object)

# Convert another date string to datetime object
date_string2 = "28-1-25"
date_object1 = datetime.datetime.strptime(date_string2, "%d-%m-%y")
print(date_object1)

# Convert datetime object to string using STRFTIME-+
year = x.strftime("%Y")
print("Year:", year)

month = x.strftime("%m")
print("Month (numeric):", month)

month1 = x.strftime("%B")
print("Month (full name):", month1)

month2 = x.strftime("%b")
print("Month (short name):", month2)

date = x.strftime("%d")
print("Day of the month:", date)

day = x.strftime("%A")
print("Weekday:", day)

time = x.strftime("%H-%M-%S")
print("Time (HH-MM-SS):", time)

date_time = x.strftime("%d %B %Y, %H:%M:%S")
print("Formatted Date & Time:", date_time)


# Format	Description
# %d	    Day of the month (01–31)
# %m	    Month (01–12)
# %B	    Full month name (e.g., July)
# %b	    Abbreviated month name (e.g., Jul)
# %Y	    4-digit year (e.g., 2025)
# %y	    2-digit year (e.g., 25)
# %H	    Hour (00–23)
# %M	    Minute (00–59)
# %S	    Second (00–59)
