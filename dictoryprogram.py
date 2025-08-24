dict1={1:10,2:20,3:30,4:40,5:50}
#print(len(dict1))

# Element adding
#dict1[6]=60
#print(dict1)
#dict1[7]=70
#print(dict1)

#updating or modify (value change)
#dict1[2]=200
#print(dict1)
#dict1[4]=400
#print(dict1)
# value print
#print(dict1[1])

# key change
student1={"name":"arun", "age":30,"place":"kuravilangad","mark1":50,"mark2":70,"mark3":90}
#student1["NAME"]=student1.pop("name")
#print(student1)

# methods
#1.get
#print(student1.get("mark3"))

#update
#print(student1.update("mark1":78,"age":25))

#popitem(remove last element
#print(student1.popitem())

#key 
#print(student1.keys())

#value 
#print(student1.values())

#item
#print(student1.items())

#only Direct looping

# only keys
#for i in student1:
    #print(i)

#only values
#for i in student1.values():
    #print(i)

# values and keys
#for i,j in student1.items():
    #print(i,j)

# input read
dict2={}
for i in range(5):
    k=int(input("Enter the keys"))
    v=int(input("Enter the values"))
    dict2.update({k:v})