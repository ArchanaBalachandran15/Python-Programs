import pickle
# define a python object
person ={"name:Arun","age:30","gender:male"}
#pickle(write) the object to binary file
#with open("person.pickle","wb") as file:
    #pickle.dump(person,file)
#print("pickling completed")

#unpickling(read) load the data from a file
with open("person.pickle","rb")as f:
    data=pickle.load(person,f)
print(data)