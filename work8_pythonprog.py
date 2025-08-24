# Some Pyhton Programms

# # Q.1: Find the sum of digits of a number.
# num = int(input("Enter a number: "))
# total = 0
# while num > 0:
#     total += num % 10
#     num //= 10
# print("Sum of digits:", total)


# # Q.2: Check if a number is prime.
# num = int(input("Enter a number: "))
# if num > 1:
#     for i in range(2, num):
#         if num % i == 0:
#             print("Not Prime")
#             break
#     else:
#         print("Prime")
# else:
#     print("Not Prime")


# # Q.3:Find largest and smallest in a list (user input)
# nums = list(map(int, input("Enter numbers separated by space: ").split()))
# largest = nums[0]
# smallest = nums[0]
# for n in nums:
#     if n > largest:
#         largest = n
#     if n < smallest:
#         smallest = n
# print("Largest:", largest)
# print("Smallest:", smallest)


# # Q.4:Count occurrences of an element in a list
# lst = input("Enter list elements only on number and the elements eparated by space: ").split()
# lst = [int(i) for i in lst]
# element = int(input("Enter element to count: "))
# count = 0
# for i in lst:
#     if i == element:
#         count += 1
# print("Count:", count)


# # Q.5: Remove duplicates from a list
# lst = input("Enter list elements separated by space: ").split()

# result = []
# for i in lst:
#     if i not in result:
#         result.append(i)

# print("Without duplicates:", result)


# # Q.6: Reverse a list without using built-in functions
# lst = input("Enter list elements separated by space: ").split()

# reversed_list = []
# for i in range(len(lst)-1, -1, -1):
#     reversed_list.append(lst[i])

# print("Reversed list:", reversed_list)


# # # Q.7: Find second-largest number in a list
# lst = input("Enter numbers separated by space: ").split()
# lst = [int(i) for i in lst]

# largest = second = float('-inf')
# for i in lst:
#     if i > largest:
#         second = largest
#         largest = i
#     elif i > second and i != largest:
#         second = i

# print("Second largest:", second)



# # Q.8: Check if a string is a palindrome
# s = input("Enter a string: ")
# s = s.lower()  # convert to lowercase

# rev = ''
# for i in range(len(s)-1, -1, -1):
#     rev += s[i]

# if s == rev:
#     print("Palindrome")
# else:
#     print("Not Palindrome")


# # Q.9: Count vowels and consonants in a string
# s = input("Enter a string: ")
# vowels_list = 'aeiouAEIOU'
# v = c = 0
# vowel_letters = ''
# consonant_letters = ''
# for ch in s:
#     if ch.isalpha():
#         if ch in vowels_list:
#             v += 1
#             vowel_letters += ch
#         else:
#             c += 1
#             consonant_letters += ch
# print("Vowels:", v)
# print("Vowel letters:", vowel_letters)
# print("Consonants:", c)
# print("Consonant letters:", consonant_letters)


# # Q.10: Reverse a number
# num = int(input("Enter a more than one digit number: "))
# rev = 0
# while num > 0:
#     rev = rev * 10 + num % 10
#     num = num // 10
# print("Reversed number:", rev)


# # Q.11: Find key with maximum value in a 
# d = {}
# n = int(input("Enter number of key-value pairs: "))

# for i in range(n):
#     key = input("Enter key: ")
#     value = int(input("Enter value: "))
#     d[key] = value

# max_key = list(d.keys())[0]
# for k in d:
#     if d[k] > d[max_key]:
#         max_key = k

# print("Result = " + max_key + ":" + str(d[max_key]))



# # Q.12: Check if number is Armstrong
# num = int(input("Enter a number: "))
# temp = num
# sum = 0
# order = len(str(num))
# while temp > 0:
#     digit = temp % 10
#     sum += digit ** order
#     temp //= 10
# if sum == num:
#     print("Armstrong number")
# else:
#     print("Not an Armstrong number")



# # Q.13: Read a text file and count number of words
# file = open("work8_1.txt", "r")
# content = file.read()
# words = content.split()
# print("Number of words:", len(words))
# file.close()

# # Q.14: Copy contents of one file to another
# f1 = open("work8_2.txt", "r")
# f2 = open("work8_1.txt", "w")
# for line in f1:
#     f2.write(line)
# f1.close()
# f2.close()
# print("File copied")


# # Q.15: Find the longest word in a text file
# file = open("work8_3.txt", "r")
# words = file.read().split()
# longest = ''
# for word in words:
#     if len(word) > len(longest):
#         longest = word
# print("Longest word:", longest)
# file.close()


# # Q.16: Print a right-angled triangle (for loop)
rows = int(input("Enter number of rows: "))
for i in range(1, rows+1):
    print("*" * i)
