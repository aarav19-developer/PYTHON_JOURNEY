'''
TYPECASTING:- 
             The process of converting a variable from one data type to another str(), int(), float(), bool().

'''

name = "Dear zindagi"
age = 19
gpa = 1322.00
code = True

print(type(name))
print(type(age))
print(type(gpa))
print(type(code))

# float into int:
gpa = int(gpa)
print(gpa)
print(type(gpa))

# int into float:
age = float(age)
print(age)
print(type(age))

# int into string:
# age = str(age)
# age += 1
 # this will give you an error as 1 is integer not a string.
# print(age)
# print(type(age))

age = str(age)
age += "1" # here string will concatenate with another string and give the result 19.01.
print(age)

