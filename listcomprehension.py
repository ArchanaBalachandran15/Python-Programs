# List Comprehension Method
# List comprehwnsion is used in code was written in short and generate a new list

# To create a new list in for loop method General method
list1 = ["apple", "orange", "mango", "grape"]
list2 = []
for i in list1:
    if "g" in i:
        list2.append(i)
print(list2)

# Method 2 List Comprehension
list3 = ["apple", "grape", "guava", "banana", "mango"]  # original list
list4 = [i for i in list3 if "g" in i]  # filter words containing 'g'
print(list4)   # pritn only in the g fruits

# Another Program carrot!=list print 
list5 = ["apple", "orange", "mango", "grape","carrot"]
list6 = [i for i in list5 if i != "carrot"]
print(list6)

# print 1-10 even numbers in list comprehension method
even_numbers = [i for i in range(2, 11, 2)]
print(even_numbers)

# Print the list5 in upper case in list comprehension method
list5 = ["Mariyam", "Surya", "Avemariya"]
list7 = [i.upper() for i in list5]
print(list7)
