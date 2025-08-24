#txt=input("enter a word")
#list1=txt.split()
#for i in list1:
    #print(i)

#count number of words 
#txt=input("enter the word")
#list1=txt.split()
#print(len(list1))

# sots the sentences
#txt=input("enter the word")
#list1=txt.split()
#list1.sort()
#print(list1)


#largest word
#txt=input("enter the word")
#list1=txt.split()
#large=list1[0]
#for i in range(1,len(list1)):
    #if len(large)<len(list1[i]):
        #large=list1[i]
#print(large)

# smallest word
txt=input("enter the word")
list1=txt.split()
small=list1[0]
for i in range(1,len(list1)):
    if len(small)>len(list1[i]):
        small=list1[i]
print(small)