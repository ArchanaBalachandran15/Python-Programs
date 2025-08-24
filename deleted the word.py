sen=input("enter the sen")
list1=sen.split()
res=[]
for i in list1:
    if i!="the":
        res.append(i)
print(" ".join(res))

