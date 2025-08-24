# sum of digits of a number
num=567
sum=0
while num>0:
    digit=num%10
    num=num//10
    sum=sum+digit
print(sum)
