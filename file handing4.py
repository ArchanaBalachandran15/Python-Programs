# line by line read
l1=[]
f=open("newfile789.txt","w")
f.write("hello how are you\n python is high level program\n object oriented program")
f.close()
f=open("newfile789.txt","r")
for i in f:
    l1.append(i.strip())
print(l1)


