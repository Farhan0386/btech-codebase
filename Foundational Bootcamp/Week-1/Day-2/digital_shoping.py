def cart():
    products_list = []

    while True:
        print("Please select an option:")
        print("1. Add item to cart")
        print("3. Checkout")
        choice = input("Enter your choice: ")

        if choice == '1':
            item_name= input("Enter the name of the item: ")
            item_quantity=int(input("Enter the quantity of the item: "))
            item_price=float(input("Enter the price of the item: "))
            products_list.append({item_name: (item_quantity, item_price)})
        elif choice=='3':
            total_price=0
            print("Items in your cart")

            for product in products_list:
                for item, details in product.items():
                    quantity, price = details
                    print(f"{item} - {quantity} @ ${price:.2f} : Total: ${quantity * price:.2f}")
                    total_price += quantity * price

            print(f"Total Price: ${total_price:.2f}")
            return
        else:
            print("Invalid choice")
cart()