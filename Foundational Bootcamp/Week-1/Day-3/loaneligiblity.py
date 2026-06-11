budget=int(input("Enter your Budget"))
emi=1200

if budget>=30000 and emi (0.4*budget):
    print("Eligble for Loan")

elif budget<3000:
    print("Income too low")

elif emi>=(0.4*budget):
    print("high debt burden")