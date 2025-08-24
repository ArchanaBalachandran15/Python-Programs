def func():
    s1=input("Enter the elements: ")
    sum=0
    for i in s1:
        if i.isdigit():
            sum+=int(i)
    print(sum)
func()