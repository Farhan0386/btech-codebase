temprature = float(input("Enter temperature in Celsius: "))

if temprature < 0:
    print("Wear a heavy coat")

elif temprature <= 15:
    print("Wear a jacket")

elif temprature <= 30:
    print("Comfortable weather")

else:
    print("Wear light clothing and stay hydrated")