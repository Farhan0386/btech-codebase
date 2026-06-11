print("UNIVERSITY ADMISSION ELIGIBILITY CHECKER")

name = input("Enter Student Name: ")
age = int(input("Enter Age: "))
percentage = float(input("Enter Class 12 Percentage: "))
exam_score = float(input("Enter Entrance Exam Score: "))
category = input("Enter Category: ")

# Eligibility
if percentage >= 60 and exam_score >= 50:
    eligibility = "Eligible"
else:
    eligibility = "Not Eligible"

# Scholarship
if percentage >= 90:
    scholarship = "100% Scholarship"
elif percentage >= 80:
    scholarship = "50% Scholarship"
elif percentage >= 70:
    scholarship = "25% Scholarship"
else:
    scholarship = "No Scholarship"

# Admission Grade
average = (percentage + exam_score) / 2

if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
else:
    grade = "D"

# Report
print("\n----- ADMISSION REPORT -----")
print("Name:", name)
print("Age:", age)
print("Category:", category)
print("Class 12 Percentage:", percentage)
print("Entrance Exam Score:", exam_score)
print("Eligibility:", eligibility)
print("Scholarship:", scholarship)
print("Admission Grade:", grade)