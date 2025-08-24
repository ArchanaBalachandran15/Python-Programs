# Reducing function example

from functools import reduce
ls=[10,20,30,40,50]
sum= reduce(lambda x,y: x+y,ls) 
print(sum)

# another method of sum 
#print(sum(ls))

# determine the maximum of a list of numerical values by using reduce:
max=reduce(lambda a,b: a if(a>b) else b,[47,105,100,15,10] )
print(max)