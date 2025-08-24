def func():
    s1=input("Enter a string")
    upper=""
    lower=""
    for i in s1:
        if i.isupper():
            upper+=i
            # print(upper)
        else:
            lower+=i
            # print(lower)
    print(lower+upper)
func()
