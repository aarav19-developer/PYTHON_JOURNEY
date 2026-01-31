# PYTHON COMPOUND INTEREST CALCULATOR:

principal = 0
rate = 0
time = 0
n = 0

while principal <= 0:
    principal = int(input("enter the principal amount: "))
    if principal <= 0:
        print("Principal can't be less than or equal to zero")

while rate <= 0:
    rate = int(input("enter the rate amount: "))
    if rate <= 0:
        print("rate can't be less than or equal to zero")

while time <= 0:
    time = int(input("enter the time: "))
    if time <= 0:
        print("time can't be less than or equal to zero")

while n <= 0:
    n = int(input("enter the  value of n: "))
    if n <= 0:
        print( "n can't be less than or equal to zero")

amount = principal*((1+rate/n)**time)
COMPOUND_INTEREST = amount - principal
print(COMPOUND_INTEREST)