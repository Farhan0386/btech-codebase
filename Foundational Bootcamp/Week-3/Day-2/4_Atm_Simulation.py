class ATM:
    def __init__(self, owner, balance=0, pin=None):
        self._owner=owner
        self.__balance=balance
        self.__pin=pin
    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount<=0:
            raise ValueError("Invalid deposit amount")
        self.__balance+=amount

    def withdraw(self, amount, pin):
        if pin!=self.__pin:
            raise ValueError("Invalid pin")
        if amount<=0:
            raise ValueError("Invalid withdrawal amount")
        if amount>self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance-=amount

user1=ATM("Farhan", 1000, "1234")
print("====================ATM Simulation====================")
print("Welcome:", user1._owner)
print("----------------------------------------------------------------")
print("Choose a option : 1. Check Balance 2. Deposit 3. Withdraw")
option=int(input("Enter your choice: "))
if option==1 or option==2 or option==3:
    if option==1:
        print("--------------------Check Balance--------------------")
        pin=input("Enter your pin: ")
        if pin==user1._ATM__pin:
            print("Balance:", user1.balance)
        else:
            print("Invalid pin")
    elif option==2:
        print("--------------------Deposit--------------------")
        pin=input("Enter your pin: ")
        if pin==user1._ATM__pin:
            amount=float(input("Enter deposit amount: "))
            user1.deposit(amount)
            print(f"{amount} Ruppes deposited. New balance: {user1.balance}")
        else:
            print("Invalid pin")
    elif option==3:
        print("--------------------Withdraw--------------------")
        pin=input("Enter your pin: ")
        amount=float(input("Enter withdrawal amount: "))
        if amount>user1.balance:
            print("Insufficient funds")
        elif amount<=0:
            print("Invalid withdrawal amount")
        elif amount>20000:
            print("Maximum withdrawal limit is 20000 Ruppes")
        elif pin==user1._ATM__pin:
            user1.withdraw(amount, pin)
            print(f"{amount} Ruppes withdrawn. New balance: {user1.balance}")
        else:
            print("Invalid pin")
    else:
        print("Invalid option.")
else:
    print("Invalid option.")   