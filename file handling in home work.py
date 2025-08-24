#function to read and count word "the"
#def func():
    #f=open("newfile123.txt","r")
    #data=f.read()
    #print(data.count("the"))
#func()


#function
#def display_words():
    #f1=open("newfile123.txt","r")
    #data1=f1.read()
    #sp=data1.split()
    #for i in sp:
        #if len(i)<3:
            #print(i)
#display_words()


#count the words
def count_words():
    f1=open("newfile123.txt","r")
    data2=f1.read()
    sp=data2.split()
    count=0
    for i in sp:
        if i[-1]=="e":
            count=count+1
    print(count)
count_words()


