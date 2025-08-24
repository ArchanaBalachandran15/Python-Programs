# swapping problem

# 1.First Method
# Using third variable temp
a=int(input("Enter the first_Number: "))
b=int(input("Enter the second_Number: "))
temp=a
a=b
b=temp
print("a" "=",a)
print("b" "=",b)

# 2.Second Method
num1=int(input("Enter the num1: "))
num2=int(input("Enter the num2: "))
num1,num2=num2,num1
print("num1" "=",num1)
print("num2" "=",num2)

# 3.Third Method
#  Using Operators 
first=int(input("Enter the first number: "))
second=int(input("Enter the second number: "))
first=first^second
second=first^second
first=first^second
print("fist", "=",first)
print("second","=",second)