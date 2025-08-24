#date and time module
import datetime
#print(datetime.datetime.now())
x=datetime.datetime.now()
print(x.strftime("%A"))
print(x.strftime("%a"))

print(x.strftime("%B"))
print(x.strftime("%b"))

print(x.strftime("%Y"))
print(x.strftime("%y"))

print(x.day)
print(x.month)
print(x.year)

y=datetime.datetime(2002,4,15)
print(y.strftime("%A"))