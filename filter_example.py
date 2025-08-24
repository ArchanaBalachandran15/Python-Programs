#filter_example

ls=[1,2,3,4,5,6,7,8,9,10,12]
result1=list(filter(lambda x : x%2==0, ls))   # filter even number
print(result1)

result2=list(filter(lambda x : x%2!=0, ls)) # filter old number
print(result2)