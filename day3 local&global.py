# LOCAL VARIABLE & GLOBAL VARIABLE

# 1.LOCAL VARIABLE: Python local variables are defined inside a function we can't access variable outside the function
def sum(x,y):
    sum=x+y
    return sum
print(sum(10,5))

# 2. GLOBAL VARIABLE: Python global variable are defined outside a function we can access variable outside and inside the function
a=20   # global variable
b=10   # global variable
def add():
    add=a+b
    return add
print(add())