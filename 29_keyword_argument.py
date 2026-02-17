# KEYWORD ARGUMENT:-
                   # An argument preceded by an identifier helps with
                   #  readability order of arguments does not matter.

def hello(greeting, title,first, last):
    print(f"{greeting} {title} {first} {last}")

hello("Hello","Ms.","DEAR","ZINDAGI")

for x in range(1,11):
    print(x,end=" ")


# TASK:
# Create a function to generate phone number:

def create_number(country,area,first,last):
    return f"{country} {area} {first} {last}"
phone_num = create_number(91,15,1322,0.806)
print(phone_num)