# Multiplication Table

# Method 1 Using print function
b = int(input("Enter the number: "))
print("1 x", b, "=", 1 * b)
print("2 x", b, "=", 2 * b)
print("3 x", b, "=", 3 * b)
print("4 x", b, "=", 4 * b)
print("5 x", b, "=", 5 * b)
print("6 x", b, "=", 6 * b)
print("7 x", b, "=", 7 * b)
print("8 x", b, "=", 8 * b)
print("9 x", b, "=", 9 * b)
print("10 x", b, "=", 10 * b)

# Method-2 For-loop
num=int(input("Enter the Number: "))
for i in range(1,11):
    print(i,"x",num,"=",num*i)

# Method-3 While Loop
mul_num=int(input("Enter the number: "))
i=1
while i<=10:
    print(i,"x",mul_num, "=", mul_num*i)
    i+=1