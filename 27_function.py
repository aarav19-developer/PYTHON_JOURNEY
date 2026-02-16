# FUNCTION:-
          # A block of reusable code place () after the function name to invoke it.

# return: 
        # statement used to end a function and send a result back to the caller.

def add(x,y):
    z= x+y
    return z
def subtract(x,y):
    z = x -y 
    return z
def multiply(x,y):
    z = x*y
    return z
def divide(x,y):
    z = x/y
    return z

print(add(13,22))
print(subtract(13,22))
print(divide(13,22))
print(multiply(13,22))

def name(first , last):
    first = first.capitalize()
    last = last.capitalize()
    return first+" "+ last
full_name = name("AARAV","HARIT-19")
print(full_name)


