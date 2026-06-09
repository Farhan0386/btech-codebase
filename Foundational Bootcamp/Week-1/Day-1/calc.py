emp_no=int(input("Enter the employee number: "))
print("\n")
def calculate_salary(emp_no):
    for i in range(1, emp_no+1):
        print(f"Employee {i}:") 
        emp_id=int(input("Enter the employee ID: "))
        emp_name=input("Enter the employee name: ")
        emp_salary=float(input("Enter the employee salary: "))
        base_salary=emp_salary
        hra=0.2*base_salary
        da=0.15*base_salary
        gross_salary=base_salary+hra+da
        tax=0.1*gross_salary
        net_salary=gross_salary-tax
        print(f"Gross Salary: {gross_salary}")
        print(f"Net Salary: {net_salary}")
calculate_salary(emp_no)


