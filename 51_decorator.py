# DECORATOR: 
#             A function that extends the behaviour of another function without modify the base function.
#             Pass the base function as an argumnt to the decorator.
#              eg: To add sprinkle on ice cream, where sprinkle is decorator and ice cream is a base function.

def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("You add sprinkles")
        func(*args, **kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("You add a fudge")
        func(*args, **kwargs)
    return wrapper

@add_sprinkles 
@add_fudge
def ice_cream(flavor):
    print(f"Here is your {flavor} ice cream")

ice_cream("Chocolate")