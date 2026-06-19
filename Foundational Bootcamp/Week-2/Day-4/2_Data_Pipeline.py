numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(numbers)
odd_numbers=list(filter(lambda x:x%2!=0, numbers))
print("-----------Odd Numbers-----------")
print(odd_numbers)
squared_odd_numbers=list(map(lambda x:x**2, odd_numbers))
print("-----------Squared Odd Numbers-----------")
print(squared_odd_numbers)
print(f"The sum of squared odd numbers is: {sum(squared_odd_numbers)}")
