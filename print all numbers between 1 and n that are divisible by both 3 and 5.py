# print all numbers between 1 and n that are divisible by both 3 and 5
z=int(input("enter the number"))
for i in range(1,z):
    if i%3==0 and i%5==0:
        print(i)

