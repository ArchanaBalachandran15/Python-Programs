# check the palindrome numbers inn 1-500
for i in range(1,500):
    temp=i
    rev=0
    while i>0:
        digit=i%10
        i=i//10
        rev=rev*10+digit
    if(temp==rev):
        print(temp)
