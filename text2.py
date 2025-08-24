import os

file_name = ""

while True:
    print("1. Create File")
    print("2. Enter Content to File")
    print("3. Read File")
    print("4. Delete File")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        file_name = input("Enter the file name: ")
        with open(file_name, "w") as f:
            pass
        print(f"{file_name} File created successfully")

    elif choice == 2:
        if file_name == "":
            print("No file created yet!")
        else:
            content = input("Enter contents to file: ")
            with open(file_name, "a") as f:
                f.write(content + "\n")
            print("Content appended successfully")

    elif choice == 3:
        if file_name == "":
            print("No file created yet!")
        else:
            with open(file_name, "r") as f:
                print(f.read())

    elif choice == 4:
        if file_name == "":
            print("No file created yet!")
        else:
            os.remove(file_name)
            print("file deleted")
            file_name = ""

    elif choice == 5:
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")
