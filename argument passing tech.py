#Arbitrary argument
 my_function(*args):
    for i in args:
        print(i)
my_function(1,2,3,4)


#keyword argument
def example(c,a,b):
    print(b)
example(a=2,b=5,c=7)


# arbitrary key argument combination
def funct2(**args):
    print(args["c"])
funct2(c=20,a=10,b=40)