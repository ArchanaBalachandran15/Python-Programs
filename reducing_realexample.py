# Reduce_Real  Example
# shopping cart
from functools import reduce
cart=[{'name':'Phone',"price":10000},{'name':'dress',"price":2000}]
cost= reduce(lambda x,y: x+y['price'] , cart, 0)
print(cost)
