txt=input("enter the string")
if len(txt)>=3:
    if txt[-3:]=="ing":
        print(txt[:-3]+"ly")
    else:
        print(txt+"ing")
else:
    print(txt)

