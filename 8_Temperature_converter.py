# TEMPERATURE CONVERTER:
Temperature = float(input("Enter your tempearture in (INTEGER or DECIMAL) value: "))
Unit = input("Enter your unit in symbol [ Kelvin(K),Celcius(C),Fahrenheit(F) ]: ")
Convert_into = input("Enter the unit [ K, C, F] in which you have to convert the temperature: ")


if Convert_into == "K" and Unit == "C":
    result = Temperature + 273.15
    print(f"The value of the {Temperature}{Unit} in Kelvin is: {round(result,2)}")
elif ( Convert_into == "F" and Unit == "C"):
    result = (9*Temperature)/5 + 32
    print(f"The value of the {Temperature}{Unit} in Fahrenheit is: {round(result,2)}")
elif(Convert_into == "K" and Unit == "F"):
    result = (5*(Temperature - 32))/9 + 273.15
    print(f"The value of the {Temperature}{Unit} in Kelvin is: {round(result,2)}")
elif(Convert_into == "C" and Unit == "F"):
    result = ((Temperature-32)*5)/9
    print(f"The value of the {Temperature}{Unit} in Celcius is: {round(result,2)}")
elif(Convert_into == "C" and Unit == "K"):
    result = Temperature - 273.15
    print(f"The value of the {Temperature}{Unit} in Celcius is: {round(result,2)}")
elif(Convert_into == "F" and Unit == "K"):
    result = (9*(Temperature-273.15))/5 + 32
    print(f"The value of the {Temperature}{Unit} in Fahrenheit is: {round(result,2)}")
elif(Convert_into == "K" and Unit == "K"):
    print("You have put the same unit in both { Convert_into and Unit} ")
elif(Convert_into == "F" and Unit == "F"):
    print("You have put the same unit in both { Convert_into and Unit} ")
elif(Convert_into == "C" and Unit == "C"):
    print("You have put the same unit in both { Convert_into and Unit} ")
else:
    print("ERROR,")
    print("HINT: May you have not captalized the Unit symbol.")

