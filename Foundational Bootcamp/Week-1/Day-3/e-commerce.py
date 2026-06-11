cart_total=int(input("Enter Cart Total: "))
subscribtion_status=input("Are you a subscribed user? (yes/no): ")
discount=0

if cart_total>=5000:
    discount=15
    if subscribtion_status=="yes":
        discount=discount+5
elif cart_total<=5000:
    discount=5

else:
    print("No discount available.")

discount_percentage=(discount/100)*cart_total

print(f"Cart Total: {cart_total}")
print(f"Discount: {discount}%")
print(f"Final: {cart_total-discount_percentage}")
