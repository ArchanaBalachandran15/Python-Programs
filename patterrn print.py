#patten print
n=int(input(" enter the number :"))
for i in range(0,n):
    for j in range(i+1):
        print("*", end=" ")
    print()

n=int(input("enter the number"))
for i in range(1,n+1):
    for j in range(i):
        print(i, end=" ")
    print()