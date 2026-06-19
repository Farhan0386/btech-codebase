class Account:
    def __init__(self, money):
        self.money = money

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount")
            return
        self.money += amount
        print("Deposited ₹", amount)

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount")
            return
        if amount > self.money:
            print("Insufficient balance")
            return
        self.money -= amount
        print("Withdrawn ₹", amount)

    def balance(self):
        print("Current Balance =", self.money)

user_account = Account(1000)
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