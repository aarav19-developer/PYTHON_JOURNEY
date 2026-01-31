# WEIGHT CONVERTER:
weight = float(input("Enter your weight: "))
unit = input("Enter unit in kilogram(kg) or gram(g): ")

if (unit == "kg"):
    result = weight * 1000
    unit = "kg"
    print(f"The weight in gram is: {result}{unit}")
elif (unit == "g"):
    result = weight / 1000
    unit = "g"
    print(f"The weight in kilogram is: {result}{unit}")
else:
    print("The unit is not valid")