# filter_real_example
product=[{'name':'samsug mobile','stock':10},{'name':'Redmi mobile','stock':50},{'name':'Nokia mobile','stock':15}]
result=list(filter(lambda prod : prod['stock']<=25,product))
print(result)


