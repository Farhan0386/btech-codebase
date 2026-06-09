def student_performace():
    student_name= input("Enter student name: ")
    student_roll_number=int(input("Enter student roll number: "))
    maths=float(input("Enter Maths Marks: "))
    physics=float(input("Enter Physics Marks: "))
    chemistry=float(input("Enter Chemistry Marks: "))
    english=float(input("Enter English Marks: "))
    computer_science=float(input("Enter Computer Science Marks: "))
    student_attendance_percentage=float(input("Enter student attendance percentage: "))
    student_assignment_score=float(input("Enter student assignment score: "))
    
    student_marks_list = [maths,physics,chemistry,english,computer_science]
    total_marks=sum(student_marks_list)
    percentage=total_marks / 5
    print("============STUDENT PERFORMANCE REPORT=============")
    print(f"Results for                 {student_name}:")
    print(f"Roll Number:                {student_roll_number}")
    print("-------------------------------------------")
    print(f"Maths Marks:                {maths}")
    print(f"Physics Marks:              {physics}")
    print(f"Chemistry Marks:            {chemistry}")
    print(f"English Marks:              {english}")
    print(f"Computer Science Marks:     {computer_science}")
    print("-------------------------------------------")
    print(f"Total Marks:                {total_marks}")
    print(f"Percentage:                 {percentage:.2f}%")

    if percentage >= 90:
        print("Grade:  A")
    elif percentage >= 80:
        print("Grade:  B")
    elif percentage >= 70:
        print("Grade:  C")
    elif percentage >= 60:
        print("Grade:  D")
    else:
        print("Grade:  F")

    if student_attendance_percentage >= 75:
        print("student is eligible for exams")
    else:
        print("student is debarded due to low attendance")

    if student_assignment_score >= 80 and percentage >= 70 and student_attendance_percentage >= 75:
        print("student is pass")
    else:      
        print("student is fail")
student_performace()