# object oriented programming:

# CLASS  : Base model,key_word is class
# OBJECT : Base model ill ninum Making products are object
# Each object has each memeory space


class MySample1:
    def hello(self):
        print("Hello Haii")
x=MySample1()                # x is defined as an object of the Mysample class
x.hello()                    # first method class calling method
MySample1.hello(x)           # another method class calling method


# Arguement passing method
class MySample2:
    def unique(self,Name):
        print("Hello" , Name)
x=MySample2()                  # x is defined as an object of the Mysample class
name="Achu"
x.unique(name)


# Inside the class variable creation
class MySample3:
    def variable(self,Name):
        self.name=Name
    def print_name(self):
        print(self.name)
x=MySample3()                     # x is defined as an object of the Mysample class
y=MySample3()
name="Achu"
x.variable(name)
y.variable('Archna')
x.print_name()
y.print_name()


