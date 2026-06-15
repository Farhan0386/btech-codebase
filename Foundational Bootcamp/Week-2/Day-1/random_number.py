import random

def generate_numbers():
    count = 0
    
    while True:
        num = random.randint(1, 10)
        count += 1
        print(f"Generated: {num}")

        if num > 7:
            break   
    print(f"\nTotal numbers generated: {count}")
generate_numbers()
