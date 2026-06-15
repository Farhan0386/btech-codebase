num1=int(input("Enter the first number: "))
print(num1)
if num1>0:
    if num1==0:
        print(f"{num1} is zero")
    elif num1%2==0:
        print(f"{num1} is a positive even number")
    else:
        print(f"{num1} is a positive odd number")
else:
    print(f"{num1} is a negative number")
