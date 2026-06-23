class Employee:
    def __init__(self, name, department="General", bonus=0):
        self.name=name
        self.department=department
        self.bonus=bonus

    def annual_summary(self):
        total_pay=30000 + self.bonus
        print("Name:", self.name)
        print("Department:", self.department)
        print("Total Pay:", total_pay)
        print("----------------------------")

emp1=Employee("Farhan", "Engineering", 5000)
emp2=Employee("Ali", "General", 3000)
emp3=Employee("Sara")

emp1.annual_summary()
emp2.annual_summary()
emp3.annual_summary()