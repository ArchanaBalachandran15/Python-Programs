# Data type Tuple

# creation pof tuple
tuple1=("winter","monsoon","summer",35,47,7,)
print(tuple1)
print(len(tuple1)) # print the length of the tuple

# to check the elemts present in tuple
tuple2=("car","scooty","van",29,90,"bus")
if "bus" in tuple2:
    print("present")
else:
    print("not_present")

# change the tuple elemts
# direct conversion of tuple is not possible the tuple was changed in list and change,remove and add the elements in tuple
tuple3 = ("robin", "anil", "archana", "libin", 42, 40, 20, 38)
list1 = list(tuple3)
list1[6] = "23"
tuple3 = tuple(list1)
print(tuple3)

# items add the tuple
tuple4=("avemariya","marriyam","surya",34,48)
list2=list