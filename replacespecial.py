def special():
    s1=input("Enter the s1 elements: ")
    news1=""
    for i in s1:
        if not i.isalnum() and i.isspace():
            news1+="#"
        else:
            news1+=i
    print(news1)
special()