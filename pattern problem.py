# pattern problem
#n=int(input("enter the number"))
#for i in range(1,n+1):
    #for j in range(n,i-1,-1):
        #print(j*2, end=" ")
    #print()

n=int(input("enter the number"))
for i in range(1,n+1):
    for j in range(i,1):
        print(j*2, end=" ")
    print()