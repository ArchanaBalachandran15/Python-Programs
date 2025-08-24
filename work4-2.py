# To create a number list and find out the sum of the list
# 21/07/2025-Monday Work = 4.2

# # # Method 1 for loop using
# n = int(input("How many numbers do you want to add?: "))
# num_list = []
# for i in range(n):
#     print("Enter number", i + 1, ": ", end="")
#     number = int(input())
#     num_list.append(number)
# total = 0
# for num in num_list:
#     total += num

# print("The sum of the numbers is:", total)


# # Method 2 List Comprehension Method used 
n = int(input("How many numbers do you want to add?:  "))
num_list = [int(input("Enter number " + str(i + 1) + ": ")) for i in range(n)]
total = 0
for num in num_list:
    total += num

print("The sum of the numbers is:", total)

