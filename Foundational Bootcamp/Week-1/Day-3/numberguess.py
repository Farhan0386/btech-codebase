number=42

while True:
    input_value=int(input("your Guess: "))
    if input_value==number:
        print("correct you guessed it")
        break
        
    
    elif input_value>number:
        print("Guess too high")
        if input_value-number>10:
            print("your guess is abve 10")
        elif number-input_value<10:
            print("your guess is under 10")
        

    elif input_value<number:
        print("Low")
        if number-input_value<10:
            print("your guess is under 10")
        elif input_value-number>10:
            print("your guess is abve 10")

    else:
        print("invalid input")