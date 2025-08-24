
# Date and Time Program

import datetime
print(datetime.datetime.today())  # today yille date  and time print yakkum

print(datetime.date.today())      # print only in date


# Format change : 27/4/2025
now=(datetime.datetime.now())
print(now.strftime('%d / %m / %Y'))

# New date User kodukkan:
x=datetime.datetime(2025,4,18)
print(x)

# differences between two dates(x,y)
y=datetime.datetime(2025,4,15)
print(y)
dif=x-y
print(dif)          