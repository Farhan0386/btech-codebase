cate="\n1.Temprature \n2.Length \n3.Weight"
Temprature="\n1.celsius \n2.farenhite"
Length="\n1.meter \n2.foot"
Weight="\n1.kilogram \n2.pounds"

categroy=int(input(f"{cate} \nChoosee a Catogry: "))

if categroy==1:
    unit=float(input("Enter your Value: "))
    form=int(input(f"From: {Temprature}: "))
    to=int(input(f"To: {Temprature}: "))

    if form==1 and to==2:
        value=((9/5)*unit)+32
    elif form==2 and to==1:
        value=(unit - 32) * 5/9

elif categroy==2:
    unit=float(input("Enter your Value: "))
    form=int(input(f"From: {Length}: "))
    to=int(input(f"To: {Length}: " ))

    if form == 1 and to == 2:
        value=unit * 3.28084
    elif form == 2 and to == 1:
        value=unit * 0.3048
      
    
else:
    unit=float(input("Enter your Value: "))
    form=int(input(f"From: {Weight}: "))
    to=int(input(f"To: {Weight}: "))

    if form == 1 and to == 2:
        value=unit * 2.20462
    elif form == 2 and to == 1:
        value=unit * 0.453592



print(f"This is Your Result : {value}")