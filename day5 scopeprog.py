# chechk scope
def check_scope():
    def do_local():
        test="local test" # test is the local  in function (assissin in this function)

    def do_non_local():
        nonlocal test
        test="non local test"

    def do_global():
        global test
        test="global test"

    test='default' 
    do_local()
    print("test value after do local: ",test)

    do_non_local()
    print("test value after non do local: ",test)

    do_global()
    print("test value after do global: ",test) 

check_scope()
print("test value after main ",test) 

# GLOBAL vekkupol yettavum Top ill ulla function return cheyum 
#  NON_LOCAL annekill thottu mubil ullathum 
# LOCAL annekill Function ente ullill (inside the function) ullathum


