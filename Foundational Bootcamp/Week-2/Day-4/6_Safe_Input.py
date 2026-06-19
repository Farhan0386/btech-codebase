while True:
    try:
        num=int(input("Enter a positive number: "))
        if num<0:
            print("Negative number not allowed")
            continue
        break
    except ValueError:
        print("Please enter a valid integer")

print("You entered:", num)