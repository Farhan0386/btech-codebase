def student_grade():
    student_name= input("Enter student name: ")
    maths=float(input("Enter Maths Marks: "))
    physics=float(input("Enter Physics Marks: "))
    chemistry=float(input("Enter Chemistry Marks: "))
    english=float(input("Enter English Marks: "))
    computer_science=float(input("Enter Computer Science Marks: "))
    
    student_marks_list = [maths,physics,chemistry,english,computer_science]
    student_marks_list.sort()
    
    total_marks=sum(student_marks_list)
    percentage=total_marks / 5

    print(f"\nResults for {student_name}:")
    if percentage >= 90:
        print("Grade is A")
    elif percentage >= 80:
        print("Grade is B")
    elif percentage >= 70:
        print("Grade is C")
    elif percentage >= 60:
        print("Grade is D")
    else:
        print("Grade is F")
        
    print(f"Highest Marks: {student_marks_list[-1]}")
    print(f"Lowest Marks: {student_marks_list[0]}")

student_grade()