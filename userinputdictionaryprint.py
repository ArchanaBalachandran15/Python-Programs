# User input the how many keyvalue pair presnt in dictionary and input the values and print the dictionary

my_dict = {}
n = int(input("How many key-value pairs you want to enter? "))

# Loop to get user input for dictionary
for i in range(n):
    print("Enter key", i + 1, ":")
    key = input()
    print("Enter value for key ", key, "':")
    value = input()
    my_dict[key] = value

print("The dictionary is:")
print(my_dict)

# Print total number of key-value pairs
print("Total key-value pairs in dictionary:", len(my_dict))




