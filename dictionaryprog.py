# Data Type = Dictionary
#23/07/2025 - wednesday - day 7


# # print one dictionary 
dict1={"name":"archana","age":23,"year":2002,"place":"kuvld"}
print(dict1)

# # Values Aceesing method
# 1. First Method
dict2={"name":"robin","age":43,"year":1895,"place":"pala"}
print(dict2["name"])
# 2. Second Method using GET 
print(dict2.get("age"))

# # Change : already exiting elemets are changes in dictionary
dict3={"name":"anil","age":39,"year":1983,"palce":"pala"}
dict3["palce"]="Theekoyi"
print(dict3)

# # For Loop in dictinary 
# Method 1
# this type loop they print only in KEYS
dict4={"name":"Libin","age":36,"year":1945,"palce":"vakkad"}
for i in dict4:
    print(i)

# Method 2 Print only in VALUES
dict5={"name":"amal","age":35,"year":1944,"palce":"maranjattupalli"}
for i in dict5.values():
    print(i)

# Method 2 Print Both in KEYS &  VALUES
dict6={"name":"mariyam","number":4707,"year":37,"palce":"vytilla"}
for i in dict6.items():
    print(i)

# To check the key present in dictionary
dict7={"vegetable":"carrot","kilo":56,"fruit":"apple","gram":90}
if "fruit" in dict7:
    print("present")
else:
    print("not present")

# To check the key-value pair present in dictionary
dict8={"animals":"pig","weig":56,"bird":"crow","hei":90}
if {"animal":"pig"} in dict8.items():
    print("present")
else:
    print("not present")

# # To add the values in dictionary
dict8 = {"color": "red", "code": 56, "food": "dosa", "price": 90}
dict8["vehicle"] = "scooty" 
print(dict8)

# # Remove Methods
# # Method 1 - Pop method
dict9 = {"food": "biriyani", "rate": "180", "drink": "sevenup", "price": 40, "shop": "ammahotel"}
if dict9["drink"] == "sevenup":
    dict9.pop("drink")
print(dict9)

# # Copy method
# method 1 - copy method
dict10={"name":"arathi","age":40,"bird":"parrot"}
dict8=dict10.copy
print(dict10)

# # del method
dict3=dict(dict4)
print(dict3)

# dictionary combine mwthod
dict11 = {"one": 1, "two": 2, "three": 3}
dict11.update(dict5)  
print(dict5)
