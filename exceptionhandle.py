# Exception handle programs
# 24/07/2025 thursdat day 8

# first prog
try:
    print(x)
except:
    print("the was error")  # inside the code was error the except block was worked

# second prog
try:
    y=100
    print(y)
except:
    print("the was eroor ") # inside the code was not error the ecxept was not worked

# third prog
try:
    print("v")
except:
    print("error")

# more than except block was created, excepted block was give specific names
try:
    print(k)
except NameError:
    print("variable k is not defined")
except:
    print("something went wrong")

# finally block concept
try:
    print(z)
except NameError:
    print("variable k is not defined")
except:
    print("something went wrong")
finally:
    print("This block is always executed")



