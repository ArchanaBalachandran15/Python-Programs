
# File operation

f=open("mariyam bus.py","wb+")                 # file creation
f=open("mariyam bus.py","w")                   # file ill condent write
f.write  ('print(" Mariyam Bus is my most favourite bus")')  
f.close()

with open("mariyam bus.py","r") as f:          # file lille condent read cheyan
    x=f.read()
print(x)





