# Function

# without passing arguments
def f1():
    print("hello")
f1()

# with passing arguments
def f2(a):      # inside the f2 function value name = parameter
    print(a)
f2("good morning")  # in function calling time they give the valu name = argument

# with passing two arguments
def f3(c,d):
    print(c+d)
f3(2,3)


# # Arbitory Functions
def f4(*e):         # * this symbol indicate : in a case where it is not known how many arguments will pass
    print(e[2])
f4(1,2,3,4,5)

# keyword argument
def f5(f,g,h):      #define in key values
    print(g)
f5(f=100,g=200,h=400)   # in key vaues they corresponding to values

# arbitory argument  # key value pair
def f6(**i):         # ** this symbol indicate : in a case where it is not known how many keyvalue will pass
    print(i["name"])
f6(name="Libin",age=38)

# default argument   # the default value will working when no arguments are passed
def f7(country="India"):   # this is deafult value
    print(country)
f7("germany")
f7("USA")
f7()

    