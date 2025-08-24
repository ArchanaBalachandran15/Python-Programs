###
for i in range(1,1000):
    num=i
    sum=0
    while num>0:
        digit =num%10
        sum +=digit**3
        num //=10
    if sum==i:
        print(i)