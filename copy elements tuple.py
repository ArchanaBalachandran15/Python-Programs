tuple1=(11,44,22,33,44,55,66,55)
list1=list(tuple1)
res=[]
for i in list1:
    if i==44 or i==55:
        res.append(i)
print(tuple(res))

tuple2=(11,[22,33],44,55)
list1=list(tuple2)
list1[1][0]=222
print(tuple(list1))