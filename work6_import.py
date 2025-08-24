# # Create the search the list item and print the list item and exit the program this features include program was created
# Menu driven program in list used in file handing
# 28/07/2025-Monday Work = 6 (file 2)
# This File is import.py file

import work6_module

def import_file():
    my_list = []

    while True:
        print("--- Menu ---")
        print("1. Create List")
        print("2. Search Item")
        print("3. Print List")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number from 1 to 4.")
            continue

        if choice == 1:
            my_list = work6_module.create_list()
        elif choice == 2:
            work6_module.search_item(my_list)
        elif choice == 3:
            work6_module.print_list(my_list)
        elif choice == 4:
            work6_module.exit_program()
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    import_file()

