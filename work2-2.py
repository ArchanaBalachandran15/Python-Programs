# Count the Character
# 18/07/2025-Friday Work = 2.2

string = input("Enter a string: ")
char = input("Enter a character to count: ")

count = 0
for i in string:
    if i == char:
        count += 1
print(count)