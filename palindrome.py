# palindrome 
num=int(input("enter the number"))
temp=num
rev=0
while num>0:
    digit=num%10
    num=num//10
    rev=rev*10+digit
if (temp==rev):
    print("palindrome")
else:
    print("not a palindrome")