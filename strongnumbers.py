num=int(input("Enter the number: "))
temp=num
sum=0

while(num>0):
    fact=1
    rem=num%10
    for i in range(1,rem+1):
        fact=fact*i
    sum=sum+fact
    num=num//10
    
if sum==temp:
    print("Strong numbers")
else:
    print("not a strong number")

