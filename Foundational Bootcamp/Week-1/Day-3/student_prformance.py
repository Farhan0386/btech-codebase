marks=int(input("Enter your marks"))

if marks>40:
    print("pass")
    if marks>=90:
        print("Distinction")
    elif marks>=75:
        print("First Divison")
    elif marks>=60:
        print("Second Divison")
    else:
        print("Thrid Divison")

else:
    print("Fail")


    
