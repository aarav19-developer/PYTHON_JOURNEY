# SUPER() :
#           Function used in a child to call methods from a a parent class (superclass). 
#           Allows you to extend the functionality of the inherited methods.

class Shape: 
    def __init__(self,color,is_filled):
        self.color = color
        self.is_filled = is_filled

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

class Square(Shape):
    def _init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

class Triangle(Shape):
    def _init__(self, color, is_filled, width,height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

circle = Circle("Yellow",True, 1322)

print(circle.color)