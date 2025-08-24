list1=[]
for i in range(4):
    item=int(input("enter the element"))
    list1.append(item)
list1.sort()
print("largest element is",list1[-1])

list1=[90,30,50,78]
larger=list1[0]
for i in range(1,len(list1)):
    if list1[i]>larger:
        larger=list1[i]
print(larger)
