# Functions are 4 type such as:

# 1. Function without argument & without return value
def rain():
    print("Rainy days,dreamy thoughts")
rain()
print("End the prog1")

# 2. Function with argument & with return value
def add(x,y):
    sum=x+y
    return sum
result=add(5,3)
print(result)
print("End the prog2")

# 3. Function without argument & with return value
def greetings():
    return 'Good Morning Have a Nice Day'
msg=greetings()
print(msg)
print("End the prog3")

# 4. Function with argument & without return value
def greet(name):
    print("Hello",name)
greet('Achu')
print("End the prog4")
