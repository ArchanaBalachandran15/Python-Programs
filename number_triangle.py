
print("NUMBER PATTERNS")

print("Pattern1: Reverse Triangle")
num1=int(input("Enter the number of  reverse triangle rows: "))
for i in range(num1,0,-1):
    for j in range(1,i+1,1):
        print(j,end=" ",)
    print()


print("..............................................................")

print("Pattern2: Right Angle Triangle")
num2=int(input("Enter the number of right angle triangle rows: "))
for i in range(1,num2+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()


print("...................................................................")

print("Pattern3: Repeating Row Number")
num3=int(input("Enter the repeating row numbwer triangle: "))
for i in range(1,num3+1):
    for j in range(i):
        print(i,end=" ")
    print()

print("...................................................................")


print("Pattern4: Continous Number")
num4=int(input("Enter the continuous triangle row numbwer triangle: "))
count=1
for i in range(1,num4+1):
    for j in range(i):
        print(count,end=" ")
        count+=1
    print()