#txt=input("enter the word")
#res=""
#for i in range(0,len(txt),2):
    #res+=txt[i]
#print(res)


# upper case
#txt=input('enter the word')
#res=""
#for i in range(len(txt)):
    #if i%2!=0:
        #res+=txt[i].upper()
    #else:
        #res+=txt[i]
#print(res)

#txt=(input("enter the word"))
#alpha=0
#digit=0
#for i in txt:
    #if i.isalpha():
        #alpha+=1
    #if i.isdigit():
        #digit+=1
#print(alpha)
#print(digit)

txt=input("enter the word")
upper=0
lower=0
for i in txt:
    if i.isupper():
        upper+=1
    if i.islower():
        lower+=1
print(upper)
print(lower)
