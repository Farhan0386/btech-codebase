def students():
    students={}
    print("Enter  a  option    | 1. Add Student    |   2. Exit")
    while True:
        student_option=int(input("Enter your option: "))
        if student_option==1:
            name=input("Enter student name : ")
            days_late=int(input("Enter the number of days late: "))
            students[name]=days_late
            print("============================================================")
            print("Enter  a  option    | 1. Add Student    |   2. Exit")
        elif student_option==2:
            break
        else: 
            print("Invalid option. Please try again.")
    return students

def calculate_fine(students):
    print("============================================================")
    print("Student Name\t\tDays Late\t\tFine")
    fine_calculation=[] 
    for name, days_late in students.items():
        fine=0
        if 5>=days_late>=1:
            fine=days_late*5
            print(f"{name}\t\t{days_late}\t\t{fine}")
            fine_calculation.append(fine)
        elif 10>=days_late>5:
            fine=days_late*10
            fine_calculation.append(fine)
            print(f"{name}\t\t{days_late}\t\t{fine}")
        elif days_late>10:
            fine=days_late*20
            fine_calculation.append(fine)
            print(f"{name}\t\t{days_late}\t\t{fine}")
        else:
            print(f"{name}\t\t{days_late}\t\tNo fine")
    return fine_calculation 
  
students=students()
fine_calculation=calculate_fine(students) 
print("============================================================")
print(f"Total fine collected: {sum(fine_calculation)}")
fine_calculation.sort()
print(f"Highest fine collected: {fine_calculation[-1]}")
print(f"Lowest fine collected:  {fine_calculation[0]}")
print(f"Average fine collected: {sum(fine_calculation)/len(fine_calculation)}")
print("============================================================")