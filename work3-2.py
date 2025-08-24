# To Make the Basic Calculation calculator using function 
# Even driven program
# 21/07/2025-Monday Work = 3.2

# Method 1: using function and looping
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b==0:
        return "cannot divide by zero !"
    return a/b

while True:
    print("1.Addition: ")
    print("2.Subtraction: ")
    print("3.Multiplication: ")
    print("4.Division: ")
    print("5.Exit: ")

    options=input("Enter your options(1-5): ")
    if options=='5':
        print("Exit the calculation: ")
        break

    num1=float(input("Enter the first number: "))
    num2=float(input("Enter the second number: "))

    if options=="1":
        print("Result = ",add(num1,num2))
    elif options=="2":
        print("Result = ",sub(num1,num2))
    elif options=="3":
        print("Result = ",mul(num1,num2))
    elif options=="4":
        print("Result = ",div(num1,num2))
    else:
        print("invalied option ! choose another option: ")
    break

# Method 2 Without use function and  used in looping
while True:
    num1 = float(input("Enter the First Number: "))
    num2 = float(input("Enter the Second Number: "))
    options = input("Enter the option (+, -, *, /): ")

    if options == "+":
        print("Result:", num1 + num2)
    elif options == "-":
        print("Result:", num1 - num2)
    elif options == "*":
        print("Result:", num1 * num2)
    elif options == "/":
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Cannot divide by zero")
    else:
        print("Invalid option")
    break