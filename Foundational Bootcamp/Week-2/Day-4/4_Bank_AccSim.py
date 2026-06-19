class Account:
    def __init__(self,money):
        self.money=money
    def deposit(self,amount):
        try:
            if amount<=0:
                raise ValueError("Invalid amount")

            self.money+=amount
            print("Deposited ₹",amount)

        except ValueError as e:
            print(e)
    def withdraw(self,amount):
        try:
            if amount<=0:
                raise ValueError("Invalid amount")
            if amount>self.money:
                raise Exception("Insufficient balance")
            self.money-=amount
            print("Withdrawn ₹",amount)
        except ValueError as e:
            print(e)
        except Exception as e:
            print(e)
    def balance(self):
        print("Current Balance =",self.money)

user_account=Account(1000)
user_account.deposit(500)
print("----------------------------------")
user_account.balance()
user_account.withdraw(200)
print("----------------------------------")
user_account.balance()
user_account.withdraw(2000)
user_account.deposit(-100)
print("----------------------------------")
user_account.withdraw(100)
user_account.balance()