txt=input("enter the word")
res=""
for i in txt:
    if i.isdigit():
        res+=i
print(res)