# List comprehension example

# Map and Filter are combined form is List Comphresion

number=[1,2,3,4,5]
# method 1 FOR LOPP

#double_odd=[]
#for i in number:
#   if i % 2 == 1:
 #       double_odd.append(i*2)
  #  print(double_odd)

# method 2 Functional Method

#filter_data=filter(lambda n: n%2==1,number)
#double_odd=list(map(lambda n: n*2, filter_data))
#print(double_odd)

# LIST COMPREHENSION

double_odd=[n*2 for n in number if n % 2==1]
print(double_odd)