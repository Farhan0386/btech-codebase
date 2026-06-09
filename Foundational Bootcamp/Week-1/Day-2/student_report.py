def student_report():
    student_name=str(input("student_name: "))
    roll_no=int(input("roll_no: "))
    age=int(input("age: "))
    programe=str(input("programe: "))
    cgpa=float(input("cgpa: "))
    completed_course=int(input("completed_course: "))

    remaining_course=40-completed_course
    completion_percentage=(completed_course/40)*100

    print()
    print("===Student Report===\n")
    print(f"student_name: {student_name}")
    print(f"roll_no: {roll_no}")
    print(f"age: {age}")
    print(f"programe: {programe}")
    print(f"cgpa: {cgpa}")
    print(f"Completed Course: {completed_course}")
    print(f"Remaining_course: {remaining_course}")
    print(f"completion_percentage: {completion_percentage}")

    if cgpa>=8.5:
        print("Scholarship Status: Eligible")

    else:
        print("Scholarship Status: Not eliglbe")

student_report()