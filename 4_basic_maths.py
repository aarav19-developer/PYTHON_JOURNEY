# SUM:-
a = 18 
a +=1
print(a)

# SUBTRACTION:-
b = 20
b -= 1
print(b)

# MULTIPLICATION:-
a = 11
b = 2
print(a*b)

# DIVISION:-
a = 44
b = 2
print(a/b)

# EXPONENT:-
a = 2
b = 4
c = 6
print(a**b+c)

# MODULUS:-
a = 22
b = 2
print(a%b) # only provide remainder.

# ROUND FUNCTION:-
a = 3.14
b = round(a) # round function is used to round off the value.
print(b)

a1 = 22.5
b1 = round(a1)
print(b1)

# NOTE:- if the value is in the middle as shown above then round function will choose backward number.

# ABSOLUTE FUNCTION:-
a2 = -22
b3 = abs(a2) # abs means absolute function which tell us how far the value from the zero in real number line.
print(b3)

# POWER FUNCTION:-
x = pow(4,3) # in this first we have to put base then its index.
print(x)

# MAXIMUM FUNCTION & MINIMUM FUNCTION:-
y = 21
h = 19
k = 22
print(max(y,h,k))
print(min(y,h,k))


import math

# Value of pi:-
o= math.pi
print(o)

# Value of exponent:-
print(math.e)

# Square root function:-
w = 0.9
u = 9.9
s = math.sqrt(w)
print(s)

# Ceil function:-
s1 = math.ceil(u) # Ceil function act as round of function but in forward direction.
print(s1)

# Floor function:-
s22 = math.floor(u) # floor function round of the value in backward direction.
print(s22)

# NOTE:- ceil & floor function are sub set of round function.
# Round function up the value when it is greater than equal to 0.5.
# Round function down the value when it is less than to 0.5.

# TASK:-

# CALCULATE THE CIRCUMFERENCE OF THE CIRCLE.
# radius = float(input("Enter your radius: "))
# circumference = 2*math.pi*radius
# print(f"Circumference is the circle is: {circumference} cm")

# AREA OF THE CIRCLE:-
# r1= float(input("Enter your radius: "))
# Area = math.pi*r1**2
# print(f"Area of the circle is: {Area} cm^2")

# HYPOTENEUS OF THE RIGHT ANGLE TRIANGLE:-
base = float(input("Enter the value of base of the right angled triangle: "))
perpendicular = float(input("Enter the value of perpendicular of the right angled triangle: "))
hypoteneus = math.sqrt(pow(base,2) + pow(perpendicular,2))
print(f"The hypoteneus of the right angled triangle is: {round(hypoteneus,2)} cm")












