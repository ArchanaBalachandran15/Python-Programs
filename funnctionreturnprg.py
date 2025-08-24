#def calcula():
    #a=int(input("Enter the number"))
    #b=int(input("Enter the number"))
    #return a+b,a-b,a*b,a/b
#x,y,z,q=calcula()
#print(x,y,z,q)

#factorial of a number with arguments
num=int(input())
def fat(num):
    fact=1
    for i in range(1,num+1):    
         fact=fact*i
    return fact
s=fat(num)
print(s)
