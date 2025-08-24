num1=float(input("Enter the Fisrt Number: "))
num2=float(input("Enter the Second Number: "))
opt=input("Enter the Operators(+,-,*,%,/): ")

if opt=="+":
    print(num1+num2)
elif opt=="-":
    print(num1-num2)
elif opt=="*":
    print(num1*num2)
elif opt=='%':
    print(num1%num2)
elif opt=="/":
    print(num1/num2 if num2!=0 else "cannot divided by zero")
else:
    print("Invalid operator")