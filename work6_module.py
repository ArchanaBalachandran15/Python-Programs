# Create the search the list item and print the list item and exit the program this features include program was created
# Menu driven program in list used in file handing
# 28/07/2025-Monday Work = 6 (file 1)
# This File is module.py file

def create_list():
    n = int(input("How many items you want to add? "))
    my_list = []
    for i in range(n):
        item = input("Enter item " + str(i + 1) + ": ")
        my_list.append(item)
    print("Newly created list:", my_list)
    print("List created successfully.")
    return my_list

def search_item(my_list):
    if not my_list:
        print("List is empty. Please create it first.")
    else:
        item = input("Enter item to search: ")
        if item in my_list:
            print("Item found in the list.")
        else:
            print("Item not found.")

def print_list(my_list):
    print("Current List:", my_list)

def exit_program():
    print("Exiting program. Goodbye!")

