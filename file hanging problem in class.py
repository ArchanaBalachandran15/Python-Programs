# count number of words in a text file
f=open("new file 345.txt","w")
data1=f.write("python is a high level programming object oriented language")
f.close()
f1=open("new file 345.txt","r")
data2=f1.read()
list1=data2.split()
print(len(list1))



# account upper and lower case

f=open("new file 345.txt","w")
data=f.write("Python is high level program")
f.close()
f1=open("new file 345.txt","r")
data2=f1.read()
upcount=0
low_count=0
for i in data2:
    if i.isupper():
        upcount=upcount+1
    elif i.islower():
        low_count=low_count+1
print("number of upper case:",upcount)
print("lower count:",low_count)
