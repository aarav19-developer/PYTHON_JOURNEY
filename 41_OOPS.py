# OOPS ( OBJECT ORIENTED PROGRAMS ):-

# OBJECT: A "bundle" of related attributes (variable) and methods (functions).
#        Eg: phone, cup, book, etc.
#        You need a "class" to create many objects.

# CLASS: (blueprint) used tp design the structure and layout of an object.


class Car:
    def __init__(self,model,year,color,for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

car1 = Car("Rolls Royce", 2026, "Black", False)
car2 = Car("BMW", 2026, "Black", False)
car3 = Car("G-Wagon", 2026,"Black",False)

print(car1.model)
print(car1.year)
print(car1.for_sale)

print(car2.model)
print(car2.year)
print(car2.for_sale)







