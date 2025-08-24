# Print the 1-1000 Armstrong number
# 18/07/2025-Friday Work = 2.1

# Correcct Method 1
for i in range(1,1001):
    num_str=str(i)
    digits=len(num_str)
    sum=0

    for dig in num_str:
        sum+=int(dig)**digits
    if sum==i:
        print(i)
        
# # Method 2
print("Armstrong numbers between 1 and 1000 are: ")
for i in range(1, 1000):
    digits = i
    a = digits % 10
    b = (digits // 10) % 10
    c = (digits // 100) % 10
    if i == a**3 + b**3 + c**3:
        print(i)


# Method 3
print("Armstrong numbers between 1-1000 are:")
for i in range(1, 1000):
    temp = i
    sum = 0
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp = temp // 10
    if sum == i:
        print(i)

