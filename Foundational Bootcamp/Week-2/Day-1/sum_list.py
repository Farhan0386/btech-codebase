user_input = input("Enter a sequence of numbers separated by commas: ")
items = user_input.split(",")
total_sum = 0
for item in items:
    try:
        number = float(item.strip())
        total_sum += number
        
    except ValueError:
        print(f"\nError: '{item.strip()}' is not a valid number")
        break    
print(f"The total sum of the valid numbers is: {total_sum}")