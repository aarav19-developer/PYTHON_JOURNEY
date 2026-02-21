# LIST COMPREHENSION:-
                    # A concise way to create lists in python.
                    # Compact and easier to read than traditional loops 
                    # (expression for value in iterable if condition).

doubles = []
for x in range(1,11):
    doubles.append(x*2)

print(doubles)

#----------------------- NXT ONE ----------------------#
double = [x*2 for x in range(1,11)]
print(double)

triple = [ y*3 for y in range(1,11)]
print(triple)

square = [ z*z for z in range(1,11)]
print(square)
 
#----------------------- NXT ONE ----------------------#

fruits = [ "apple","banana","coconut"]
fruits = [fruit.upper() for fruit in fruits]
fruit_chars = [fruit[0] for fruit in fruits]
print(fruits)
print(fruit_chars)

#----------------------- NXT ONE ----------------------#

numbers = [1,2,3,4,5,6,7]
negative_num=[num<0 for num in numbers]
negative_nums=[num for num in numbers if num<0]
print(negative_num)
print(negative_nums)

#----------------------- NXT ONE ----------------------#
grades = [ 9,100,99,54,13,22,80]
passing_grade=[grade for grade in grades if grade > 33]
print(passing_grade)
