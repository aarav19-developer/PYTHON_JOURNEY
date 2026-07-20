# PROPERTY:  
            # Decorator used to define a method as a property (it can be access like an attribute)
            # Benefit: Add additional logic when read, write, or delete attributes.
            # Gives you getter, setter, and deleter method. 

class Rectangle: 
    def __init__(self, width, height):
        self._width = width 
        self._height = height

    @property
    def height(self):
        return self._height

    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width

        else:
            print("Width must be greater than 0")
            
    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height

        else:
            print("Height must be greater than 0")

    # Same way deleter will also there.
    
        

rectangle = Rectangle(13,22)
rectangle.height = -1

print(rectangle._width)
print(rectangle._height)