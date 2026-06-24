class ATM:
    def __init__(self, owner, balance, pin):
        self._owner=owner
        self.__balance=balance
        self.__pin=pin

        @property
        def balance(self, pin):
            if pin!=self.__pin:
                raise ValueError("Invalid pin")
            return self.__balance

        def deposit(self, amount):
            if amount<=0:
                raise ValueError("Invalid deposit amount")
            self.__balance+=amount

        def withdraw(self, amount,pin):
            pin=input("Enter your pin: ")
            if pin!=self.__pin:
                raise ValueError("Invalid pin")
            if amount<=0:
                raise ValueError("Invalid withdrawal amount")
            if amount>self.__balance:
                raise ValueError("Insufficient funds")
            self.__balance-=amount

user1=ATM("Farhan", 1000, "1234")
print("Owner:", user1._owner)
print("Choose a option:")
print("1. Check Balance")
print("2. Deposit")
print("3. Withdraw")
option=int(input("Enter your choice: "))
pin=input("Enter your pin: ")
try:
    if option==1:
        print("Balance:", user1.balance(pin))
    elif option==2:
        amount=float(input("Enter deposit amount: "))
        user1.deposit(amount)
        print("Deposit successful.")
    elif option==3:
        amount=float(input("Enter withdrawal amount: "))
        user1.withdraw(amount, pin)
        print("Withdrawal successful.")
except ValueError as e:
    print(e)    