# File Handing
#  1. Read Mode
# # # Open file in read mode  "r"        # the code was correct
# f = open("text1.txt", "r")
# # print("Full content:",f.read())   # Read entire content
# # print("First 3 characters:",f.read(3))  # Read first 3 characters 
# # print("Read one line:",f.readline())  # Read one line

# for i in f:     # # Read using for loop (line by line)     # error check cheyanam
#     print(i)  # end='' to avoid double newlines
# f.close()  # Close the file

# # Update Mode
# #  2.Update the exiting text file  "a"
# Open file in write mode
# already ulla text2.txt file ill python django ennu add yakkum      # the code was correct
# f=open("text1.txt","a") 
# f.write("python django")
# f.close()
# f=open("text1.txt","r")
# print(f.read())
# f.close()

# # 3.Write Mode already ulla file ill write cheyan
# # # Open file in write mode  "w"                         # the code was corret
# # another text file ill annu ethu cheyithirikkunnathu text3.txt yill anuu work che u kka
# f=open("text3.txt","w")               
# f.close()
# f=open("text3.txt","r")
# f.close()

# # new text file create cheyan 
# f=open("text4.txt","x")

# import os
# os.remove("text4.txt")

# apply condition
import os 
if os.path.exists("text4.txt"):
    os.remove("text4.txt")    # evide file remove cheyitha sheshan anu file uddo ellayo ennu check che u nnathu,
else:                         # athu kodu check che u pol not exit enne kannikkullu
    print("not exist")

