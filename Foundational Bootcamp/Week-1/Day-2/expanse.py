food_expense=int(input("Food_expense: "))
travel_bill=int(input("Travel_bill: "))
internet_bill=int(input("Internet_bill: "))
entertainment_bill=int(input("Entertainment_bill: "))
miscellaneous_bill=int(input("Miscellaneous_bill: "))

total = food_expense+travel_bill+internet_bill+entertainment_bill+miscellaneous_bill
remaining_amount= 15000-total

print("===================Report=====================")
print(f"Total Expenses: {total}")
print(f"Balance Left:   {remaining_amount}")
print(f"Spent:          {total}")