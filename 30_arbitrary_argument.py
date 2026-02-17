# ARBITRARY ARGUMENTS:-

# *args = allows you to pass multiple non key arguments.
# **kwargs = allows you to pass multiple keyword-arguments
        #  * unpacking operator

# ---------NXT ONE -----------#
def add(a,b):
    return a+b
print(add(1,3))  

# ---------NXT ONE -----------#
def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(add(1,3,4,4,5,5,56)) 

# ---------NXT ONE -----------#
def display_name(*args):
    for arg in args:
        print(arg, end=" ")

display_name("DEAR","ZINDAGI")

# ---------NXT ONE -----------#
def print_address(**kwargs):
    for value in kwargs.values():
        print(value)

def print_address(**kwargs):
    for keys in kwargs.keys():
        print(keys)
    
def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")
    
print_address(street="0806",city="Meerut",state ="UP",pincode = "2501013")

# ------------------------------------NXT ONE ---------------------------------#

def shipping_label(*args,**kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    for value in kwargs.values():
        print(value, end=" ")

shipping_label("Dr.","S",
               street = "2 Delhi Road", 
               city = "Meerut",
               state = "UP",
               pin = "250103"
               )