# check if a number is prime
#n=int(input("enter a number"))
#if n<=1:
   # print("is not a prime number")

#elif n<=2:
    #print("is a prime number")
#elif n%2==0 or n%3==0:
    #print("not a prime number")
#else:
    #print("is a prime number")

 
# correct answer
n=int(input("enter a number"))
count=0
if i in range(1,n+1):
    if n%2==0:
      count+=1
if count==2:
    print("prime number")
else:
    print("not a prime")
    
