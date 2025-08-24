num=int(input("enter a number"))
temp=num
sum=0
while(num>0):
    digit=num%10
    num=num//10
    sum+=digit**3
if(temp==sum):
    print("number is armstrong ")
else:
    print("not armstrong")