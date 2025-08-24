# To checck the largest number in three numbers
# 17/07/2025-Thursday Work = 1.1

num1=int(input("Enter the num1: "))
num2=int(input("Enter the num2: "))
num3=int(input("Enter the num3: "))

if (num1>num2 and num1>num3):
    print("num1 is largest number",num1)
elif (num2>num1 and num2>num3):
    print("num2 is the largest number",num2)
else:
    print("num3 is the largest number",num3)