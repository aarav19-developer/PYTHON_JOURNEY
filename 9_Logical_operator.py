# LOGICAL OPERATOR :- evaluate multiple conditions( and, or, not)
                    # OR - atleast one condiiton must be true.
                    # AND - both condition must be true.
                    # NOT - inverts te condiiton ( not False, not True)

temperature = float(input("enter your temperature: "))
if temperature > 50 or temperature < 0:
    print("The event is cancelled")
else: 
    print("The event is scheduled")

temp = float(input("enter your temperature: "))
if temp <= 50 and temp >= 0:
    print("The event is cancelled")
else: 
    print("The event is scheduled")