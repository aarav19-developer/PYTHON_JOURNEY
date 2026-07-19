# STATIC METHOD: 
#                A method that belong to a class rather than any object from that class (instance).
#                Usually used for general utility functions.

# Instance Method : Best for operations on isntance of the class (objects).
# Static Method : Best for utility functions that do not need access to class data. 

class Employee:
    def __init__(self,name,position):
        self.name = name 
        self.position = position

    def get_info(self):
        return f"{self.name} = {self.position}"
    
    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Cook", " Janitor"]
        return position in valid_positions
    

employee1  = Employee("dear", "Doctor")
employee2  = Employee("S", "owner")
employee3  = Employee("a", "sweet")


print(Employee.is_valid_position("Cook"))

print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())