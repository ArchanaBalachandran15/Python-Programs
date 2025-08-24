# tuple prg
#tuple1=(1,25,75,"hello",85,"hai",71)
#negative indexing
#print(tuple1[-1])
#positive indexing
#print(tuple1[3])

# tuple change to list
#list1=list(tuple1)
#list1.append(100)
#list1.remove(85)
#print(len(list1))
#print(list1)

#unpacking
#tuple1=(1,2,7,8,9,5,3)
#a,b,c,d,e,f,g=tuple1
#print(a,b,c)

#4th element in tuple
#tuple1=(91,2,3,4,5,6,7)
#print(tuple1[3])
#print(tuple1[-4])

#tuple1=(12,13,12,15,19,20,20)
#rep=0
#res=[]
#for i in tuple1:
    #if i not in res:
        #res.append(i)
    #else:
        #rep+=1
#print(rep)

#remove the empty tuple
list1=[90,("a,b"),("a","b","c"),("d"),()]
res=[]
for i in list1:
    if i!=():
        res.append(i)
print(res)
