def convert_length(value, from_unit, to_unit):
    if from_unit == "m" and to_unit == "ft":
        return value * 3.28084
    elif from_unit == "ft" and to_unit == "m":
        return value * 0.3048
    else:
        return None

def convert_weight(value, from_unit, to_unit):
    if from_unit == "kg" and to_unit == "lb":
        return value * 2.20462
    elif from_unit == "lb" and to_unit == "kg":
        return value * 0.453592
    else:
        return None

def convert_temperature(value, from_unit, to_unit):
    if from_unit == "C" and to_unit == "F":
        return (value * 9/5) + 32
    elif from_unit == "F" and to_unit == "C":
        return (value - 32) * 5/9
    else:
        return None

print("Simple Unit Converter")
category = int(input("Choose category:\n1.length \n2.weight \n3.temp:\n "))
value = float(input("Enter value: "))
from_unit = input("From unit (m,ft,kg,lb,C,F,): ")
to_unit = input("To unit (m,ft,kg,lb,C,F,): ")

if category == 1:
    result = convert_length(value, from_unit, to_unit)
elif category ==2:
    result = convert_weight(value, from_unit, to_unit)
elif category ==3:
    result = convert_temperature(value, from_unit, to_unit)
else:
    result = None

if result != None:
    print(f"{value} {from_unit} = {result:.2f} {to_unit}")
else:
    print("Conversion not available.")
