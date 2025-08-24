# expense tracker using function
expenses={}
wallet=1000
while(True):
    print("menu")
    print("1.add expenses\n","2.add balances\n","3.view expense\n","4.exit\n")
    option=int(input("enter the option"))
    if option==1:
        expname=(input("enter the expense name"))
        expamount=int(input("enter the expense amount"))
        if expamount<=1000:
            if expname in expenses:
                wallet-=expamount
                expamount=expamount+expenses[expname]
                expenses[expname]=expamount
                print(expenses)
            else:

                expenses[expname]=expamount
                wallet-=expamount
                print(expenses)
                print(wallet)

        else:
            print("balance is low")
       
    elif option==2:
        addamount=int(input("enter the add amount"))
        wallet+=addamount
        print(wallet)
    elif option==3:
        print(expenses)
    else:
        exit()
    
    
