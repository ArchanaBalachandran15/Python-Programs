# armstrong number with in a range(1=100)
print("Armstrong numbers between 1 and 1000 are:")
for i in range(1, 1000):
    temp = i
    sum = 0
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp = temp // 10
    if sum == i:
        print(i)

