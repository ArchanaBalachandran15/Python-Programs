s1=input("Enter the string elements: ")
s2=input("Enter the string elements: ")
def func(s1,s2):
    for i in s1:
        if i not in s2:
            Flag=False
        if Flag==True:
            print("Balances")
        else:
            print("not balanced")


