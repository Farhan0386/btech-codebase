age=int(input("Enter your age: "))
degree=input("Enter your degree: ")
cgpa=float(input("Enter your CGPA: "))


if 41>=age>=21:
    if degree=="Bachelors" or degree=="Mca":
        if cgpa>=7.0:
            print("Interview shortlisted")
        else:
            print("not enough CGPA.")
    else:
        print("You are not eligible, you dont have degree .")
else:
    print("your age is not within the range.")

