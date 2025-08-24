#Demonstrate banking operations

class Banking_operations:
    def __init__(self):
        self.holder=""
        self.number=""
        self.available_balance=0
    
    def Details(self):
        self.holder=input("Enter the Holder Name: ")
        self.account=int(input("Enter the Account number: "))
        self.balances=int(input("Enter the balances"))

    def Deposit(self):
        deposit_amount=int(input("Enter the Deposit Amount: "))
        self.available_balance+=deposit_amount
        print("The Deposit amount is:",self.available_balance)

    def Withdraw(self):
        withdraw_amount=int(input("Enter the Withdraw amount: "))
        if withdraw_amount>self.available_balance:
            print("Insufficient balances in your account")
        else:
            self.available_balance-=withdraw_amount
            print("Withdraw cash",self.available_balance)


class Savings_account(Banking_operations):

    def cal_interest(self):
        self.principle=int(input("Enter the Interest"))
        self.num=int(input("Enter the number of year: "))
        self.final=self.principle*self.num*(4/100)
        print("New Balances:",self.final)


class Fixed_acount(Banking_operations):

    def calculate_interest(self):
        self.principle=int(input("Enter the the amount: "))
        self.num=int(input("Enter the number of year: "))
        self.final=self.principle*self.num(7/100)
        print("New balances:",self.final)



obj=Banking_operations()
obj.Details()
obj.Deposit()
obj.Withdraw()

sav=Savings_account()
sav.cal_interest()

fix=Fixed_acount()
fix.calculate_interest()
