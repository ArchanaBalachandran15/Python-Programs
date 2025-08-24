list1=[9,12,15,10,9,6,3,13,14,]
l=int(input("enter the lower limit"))
u=int(input("enter the upper limit"))
count=0
for i in list1:
    if i>l and i<u:
        count+=1
print(count)
    
