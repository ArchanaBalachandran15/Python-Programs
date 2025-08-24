
print("Star Paatterns ")

print("Pattern 1: Right Angle TRiangle")
num1=int(input("Enter the number of rows: "))
for i in range(1,num1+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print(" ")

print("................................................")

print("Pattern 2: Inverted Right Angle Triangle")
num2=int(input("Enter the number of rows: "))
for i in range(num2,0,-1):
    for j in range(1,i+1):
        print("*",end=" ")
    print(" ")

print("................................................")

print("Pattern 3: Pyramid Patter")
num3=int(input("Enter the number of rows: "))
for i in range(0,num3):
    for j in range(0,num3-i-1):
        print(end=" ")
    for k in range(0,i+1):
        print("*",end=" ")
    print()

print("................................................")


print("Pattern 3: Diamond Pattern")
num4=int(input("Enter the number of rows: "))
# upper pyramind
for i in range(1,num4):
    for j in range(1,num4-i):
        print(" ",end=" ")
    for k in range(0,2*i-1):
        print("*",end=" ")
    print()

# lower pyramind
for i in range(num4-2,0,-1):
    for j in range(1,num4-i):
        print(" ",end=" ")
    for m in range(1,(2*i)):
        print("*",end=" ")
    print()