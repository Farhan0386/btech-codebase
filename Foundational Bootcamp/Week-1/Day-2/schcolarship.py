def schcolarship():
    student_name=input("Enter student name :")
    student_age=int(input("Enter student age :"))
    student_12th_percentage=float(input("Enter student class 12th percentage :"))
    student_entrance_exam_score=float(input("Enter student Entrance Exam Score :"))
    student_category=input("Enter student category")
    print("============STUDENT SCHOLARSHIP REPORT=============")
    if student_entrance_exam_score>=75 and student_12th_percentage>=75 :
        print(f"Student  {student_name} is Eligible")
        print("Scholarship Status Eligible")
    else:
        print("Student is not Eligible")
    return
schcolarship()