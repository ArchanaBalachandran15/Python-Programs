# fibanacci series
# Class work
#21/07/2025 - monday - day 5

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b

terms = int(input("Enter the number of terms: "))
print("Fibonacci series:")
fibonacci(terms)
