# Single line string
a="Python Programming Language"
print(a)

# Multi-Line String
b = '''Python,
HTML
JavaScript
CSS
Dajngo'''
print(b)

# Check the Length of the string
c="Python is High level language"
print(len(c))

#Characher Accesing- Positive Indexing Method
d="Python is the userfriendly language"
print(d[2])  # single indexing
print(d[2:7]) # Multiple character Acessing method
print(d[:8]) # Starting index kodukathe 
print(d[1:]) # Ending Index kodukathe

#Characher Accesing- Negative-Indexing Method
e="Python is the userfriendly and easy to handle"
print(e[-4])  # single indexing
print(e[-5:7]) # Multiple character Acessing method
print(e[:-6]) # Starting index kodukathe 
print(e[-4:]) # Ending Index kodukathe

# STRING METHODS
# 1. Convertion Method
f="Python programing language is the high level multipurposes language"
print(f.upper())
print(f.lower())

# 2.Replace Method
print(f.replace("Python","full stack python"))

# 3. Split Method
print(f.split(","))

# 4.Combain
g="Full Stack Python"
h="Dajngo With React"
print(g+h)
print(a+ " "+b)

# 5. Conversion
# String Converted to Integre

# 1.Second Method
age1=42
text1="My Name is Robin and My Age is",str(age1)
print(text1)

# 2.Second Method
age2=40
text2="My Name is Anil and My Age is",age2
print(text2)

# 3.Third Method
age3=36
text3='My Name is Libin and My Age is {}'
print(text3.format(age3))
