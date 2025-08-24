# Create the search the list item and print the list item and exit the program this features include program was created
# Menu driven program in list
# 22/07/2025-Tueaday Work = 4.1

my_list = []

while True:
    print("1. Create List")
    print("2. Search Item")
    print("3. Print List")
    print("4. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        n = int(input("How many items you want to add? "))
        my_list = [input("Enter item " + str(i + 1) + ": ") for i in range(n)]
        print("Newly created list:",my_list)
        print("List created successfully.")

    elif choice == 2:
        if not my_list:
            print("List is empty. Please create it first.")
        else:
            item = input("Enter item to search: ")
            if item in my_list:
                print("Item found in the list.")
            else:
                print("Item not found.")

    elif choice == 3:
            print("Current List:",my_list)
           
    elif choice == 4:
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please enter 1 to 4.")
