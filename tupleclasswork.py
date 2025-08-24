n = int(input("How many elements do you want in the tuple? "))
elements = []
for i in range(n):
    item = input("Enter element " + str(i+1) + ": ")
    elements.append(item)

my_tuple = tuple(elements)
print("Your tuple is:", my_tuple)

search_item = input("Enter the element you want to count: ")
count = my_tuple.count(search_item)
print(search_item +  "' = " + str(count) + " times apper in the tuple.")