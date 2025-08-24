#try:
    #print(a)
#except:
    #print("something wrong")

try:
    a=10
    if a<30:
        print(a,"is greater",b)
    else:
        print(a+"")
#except NameError:
    #print("name is not defined")
#except IndexError:
    #print("Index is not found")
#except TypeError:
    #print("Type is not defined ")
#except ValueError:
    #print("Value is not defined")
#except:
    #print("Something went wrong")

except Exception as e:
    print(e)