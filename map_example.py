# map function
def double(num):
    return num*2

def square(num):
    return num**2

intput_seq=(2,3,4,5,6,7)

double_list=list(map(double,intput_seq))
print(double_list)

square_list=list(map(square,intput_seq))
print(square_list)


#Lamda function

intput_seq=(2,3,4,5,6,7)

double_list=list(map(lambda num: num*2,intput_seq))
print(double_list)

square_list=list(map(lambda num: num*2,intput_seq))
print(square_list)

