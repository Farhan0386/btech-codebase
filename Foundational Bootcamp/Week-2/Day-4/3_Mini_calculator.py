def make_operator(op):
    if op == "+":
        return lambda x, y: x + y
    elif op == "-":
        return lambda x, y: x - y
    elif op == "*":
        return lambda x, y: x * y
    elif op == "/":
        return lambda x, y: x / y
    else:
        print("Invalid operator")
x=float(input("Enter first number: "))
op=input("Enter operator (+, -, *, /): ")
y=float(input("Enter second number: "))
operation=make_operator(op)
result=operation(x, y)
print(f"The result of {x} {op} {y} is: {result}")