sen=input("enter a word")
word=sen.split()
res=[]
for i in word:
    if i not in res:
        res.append(i)
print(" ".join(res))
