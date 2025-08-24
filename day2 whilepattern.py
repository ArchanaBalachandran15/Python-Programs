num=int(input("Enter the number of rows : "))
i=0
while i<num:
    space=num-i-1
    while space>0:
        print(end=" ")
        space=space-1
    star=i+1
    while star>0:
        print("*",end=" ")
        star=star-1
    i=i+1
    print()


