# Bank Accont Prroblem in OOPS (Object orientedd programming language)

class Account:
    def __init__(self):
        self.name = input("Enter your name: ")
        self.acc_number = input("Enter your account number: ")
        self.balance = int(input("Enter your current balance: "))

    def withdraw_amount(self):
        amount = int(input("Enter the amount you want to withdraw: "))
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print("You have successfully withdrawn", amount)

    def deposit_amount(self):
        amount = int(input("Enter the amount you want to deposit: "))
        self.balance += amount
        print("You have successfully deposited", amount)

    def show_balance(self):
        print("Current Balance:", self.balance)

def main():
    acc = Account()                
    acc.withdraw_amount()
    acc.deposit_amount()
    acc.show_balance()

if __name__ == "__main__":
    main()
