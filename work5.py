# Create dictionary and the search the dictionary items and print the key,value and key-value pair present in dictionary and exit the program this features include program was created
# Menu driven program in dictionary
# 23/07/2025-Wednesday Work = 5.1

my_dict = {}

while True:
    print("1. Create Dictionary")
    print("2. Search")
    print("3. Print Dictionary")
    print("4. Exit")

    options = int(input("Enter your choice: "))

    if options == 1:
        n = int(input("How many key-value pairs you want to add?:  "))
        for i in range(n):
            key = input("Enter key " + str(i + 1) + ": ")
            value = input("Enter value for key '" + key + "': ")
            my_dict[key] = value
        print("Newly created list:",my_dict)
        print("Dictionary created successfully.")

    elif options == 2:
        if not my_dict:
            print("Dictionary is empty. Please create it first.")
        else:
            print("Search Options: ")
            print("a. Search by Key")
            print("b. Search by Value")
            print("c. Search by Key-Value Pair")
            choose = input("Choose an option (a/b/c): ").lower()

            if choose == 'a':
                search_key = input("Enter key to search: ")
                if search_key in my_dict:
                    print("Key found:", search_key, "→", my_dict[search_key])
                else:
                    print("Key not found.")

            elif choose == 'b':
                search_value = input("Enter value to search: ")
                if search_value in my_dict.values():
                    print("Value '" + search_value + "' found in dictionary.")
                else:
                    print("Value not found.")

            elif choose == 'c':
                key = input("Enter key: ")
                value = input("Enter value: ")
                if key in my_dict and my_dict[key] == value:
                    print("Key-Value pair found:", key, "→", value)
                else:
                    print("Key-Value pair not found.")
            else:
                print("Invalid search option. Please choose a, b, or c.")

    elif options == 3:
        print("Current Dictionary:", my_dict)

    elif options == 4:
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 4.")

