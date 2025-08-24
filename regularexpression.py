# Reegular Expression program
# r expression represnet in re 
# r expression has a buit in method

import re
text="haii welcome to dubai on june 23"


# # Search Method
# example:1
x=re.search("^hai",text)
print(x)

# example:2 condition based
if x:
 print("we have a match")
else:
 print("no match")

# example:3 condition based in dollar symbol
x=re.search(".*7$",text)
if x:
 print("we have match")
else:
 print("not match")

# # Find All Method
x=re.findall("[a-m]",text)
print(x)

#find out the digits 
# example:1
x=re.findall("\d",text) 
print(x)

#to find the text represnts a single charactor
# example:2
x=re.findall("we...me",text) 
print(x)

#after we 2 character
# example:3
x=re.findall("we.{2}o",text)  
print(x)

# example:4
x=re.findall("we.+1",text)
print(x)

# # Split Method
# example:1
x=re.split("\s",text)
print(x)

# example:2
x=re.split("\s",text,2)
print(x)

# # Sub Method
x=re.sub("\s","20",text,2)
print(x)