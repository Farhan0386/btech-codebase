def student_marks(name, marks):
    print("---------Student Marks Details-------------")
    print(f"Student Name: {name}")
    print(f"Marks: {marks}")
    print("-------------------------------------------")
name=input("Enter the name of the student: ")
marks=int(input("Enter the marks of the student: "))
student_marks(name, marks)

def add_bonus(name, marks, bonus):
    total_marks=marks + bonus
    print("---------Student Marks with Bonus-------------")
    print(f"Student Name: {name}")
    print(f"Original Marks: {marks}")
    print(f"Bonus Marks: {bonus}")
    print(f"Total Marks: {total_marks}")
    print("-----------------------------------------------")
bonus=int(input("Enter the bonus marks: "))
add_bonus(name, marks, bonus)
print()
def sum_marks(n):
    if n==0:
        return 0
    else:
        return n+sum_marks(n-1)
n=int(input("Enter a number to calculate the sum of marks from 1 to n: "))
total_sum=sum_marks(n)
print(f"The sum of marks from 1 to {n} is: {total_sum}")
print()
def square(x):
    return x**2
x=int(input("Enter a number to find its square: "))
result=square(x)
print(f"The square of {x} is: {result}")
print()
def cube(m):
    return m**3
m=int(input("Enter a number to find its cube: "))
result=cube(m)
print(f"The cube of {m} is: {result}")
print()
square1=square(x)
cube1=cube(m)
print("Choose an option:")
print("1. Display square of a number")
print("2. Display cube of a number")
choice=int(input())
if choice==1:
    x=int(input("Enter a number to find its square: "))
    print(f"The square of {x} is: {square1}")
elif choice==2: 
    m=int(input("Enter a number to find its cube: "))   
    print(f"The cube of {m} is: {cube1}")
else:    
    print("Invalid choice. Please select either 1 or 2.")
print()
def apply_function(func, value):
    return func(value)
result_square=apply_function(square, x)
result_cube=apply_function(cube, m)
print(f"The result of applying the square function to {x} is: {result_square}")
print(f"The result of applying the cube function to {m} is: {result_cube}")
