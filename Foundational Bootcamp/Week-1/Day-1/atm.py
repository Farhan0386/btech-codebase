def atm():
    balance=1000

    while True:
        print("1. Check Balance", "2. Deposit", "3. Withdraw", "4. Exit")
       
        option=int(input("choose an option: "))
    
        if option==1:
            print(f"Your balance is: {balance}")
        elif option==2:
            amount=float(input("Enter the amount to deposit: "))
            balance+=amount
            print(f"Your new balance is: {balance}")
        elif option==3:
            amount=float(input("Enter the amount to withdraw: "))
            if amount>balance:
                print("Insufficient funds")
            else:
                balance-=amount
                print(f"Your new balance is: {balance}")
        elif option==4:
            print("Exit")
            return
        else:
            print("Invalid option. Please try again.")
        
atm()