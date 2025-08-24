# LIST PROBLEMS []

list1=["apple","orange","grapes",5,8,"goosberry"]
print(list1)

# Indexing of List
print(list1[0]) # positive indexing
print(list1[-2]) # negative indexing
print(list1[1:5]) # more than items ascessing method

# change the items in list
list1[5]="banana"
print(list1)

# List print in for loop method
for i in list1:
    print(i)

# To check the any item present in the list
if "banana" in list1:
    print("present")
else:
    print("not present")   # output is present

if "papaya" in list1:
    print("present")
else:
    print("not present")     # output isnot present

# To check the count of list
print(len(list1))

# Items add in the list 
# Method 1-Append    
list1.append("mulberry")  # append method used the items added in the end of the list
print(list1)

# Method 2-Inseret
list1.insert(3,"kiwi")
print(list1)

# Items remove in the list
# Method 1-Remove
list1.remove("orange")  # remove the item in argument ppased item
print(list1)

# Method 2-Pop
list1.pop()  # remove the last item of the list
print(list1)

# Method 3-del keyword used
del list1[4]
print(list1)

# Two List combine
# Method 1 = + opper used
list2=["goa","kerala","karnataka",9,7]
list3=["jouery","trip",9,6,"tour"]
list4=list2+list3
print(list4)

# Method 2 = Append
for i in list2:
    list3.append(i)
print(i)

# Method 3 = extend 
list2.extend(list1)
print(list2)

# List Comprehension Method 
# this method is used to create a new lsit in already extend list
# Geranl method (for loop used)
list5 = ["crow", "parrot", 50, "hen", "duck", 100, "pigeon", 30]
list6 = []
for i in list5:
    if "o" in str(i):  # Convert i to string to avoid type error
        list6.append(i)
print(list6)

# Method 2 Comprehension 
list5 = ["crow", "parrot", 50, "hen", "duck", 100, "pigeon", 30]
new_list = [i for i in list5 if "o" in str(i)]
print(new_list)

# Item not present in list
list7=["carrot",50,"cabage",30,"potato","tomato",10,"apple"]
new_list2 = [i for i in list7 if i != "apple"]  # Create a new list without "apple"
print(new_list2)

# print the 1-10 even number in list comprehensive method
# Method 1
even_numbers1 = [i for i in range(1, 11) if i % 2 == 0]
print("method_1:",even_numbers1)

# Method 2
even_number2 =[i for i in range(2,11,2)]
print("method_2:",even_number2)

# The list items convert the upper case using list comprehensive method
list8=["python","java","c++","vb"]  # this method used only in string / character type words
list8=[i.upper()for i in list8]
print(list8)
