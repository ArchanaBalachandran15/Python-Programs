txt=input("enter the word")
res=txt[0]+txt[1:].replace(txt[0],"$")
print(res)