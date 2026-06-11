marks=int(input("Enter your marks: "))

if 100>=marks>90:
    print(f"Your grade is A+")
    print(f"Your CGPA is 10")

elif 89>=marks>80:

    print(f"Your grade is A")
    print(f"Your CGPA is 9")

elif 79>=marks>70:
    print(f"Your grade is B+")
    print(f"Your CGPA is 8")

elif 69>=marks>60:
    print(f"Your grade is B")
    print(f"Your CGPA is 7")

elif 59>=marks>50:
    print(f"Your grade is C")
    print(f"Your CGPA is 6")

elif 50>=marks:
    print(f"Your grade is F")
    print(f"Your CGPA is 4")

else:

    print("Invalid input. Please enter marks between 0 and 100.")


