# INHERITANCE:-
#              Allows a class to inherit attributes and methods from another class.
#              Helps with code reusability an extensibility
#               class Child(Parent)


class Animal:
    def __init__(self,name):
        self.name = name
        self.is_alive = True
    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.name} is sleeping")

class dog(Animal):
    pass


class cat(Animal):
    pass


class mouse(Animal):
    pass

Dog = dog("KUTTA")
Cat = cat("BILLI")
Mouse = mouse("RAT")

print(Dog.name)
print(Dog.is_alive)
Dog.eat()
Dog.sleep()


# MULTIPLE INHERITANCE:-
#                         inherit from more than one parent class.
#                           C(A , B)
# MULTILEVEL INHERITANCE:- 
#                         inherit from a parent which inherits from another parent
#                               C(B) <- B(A) <- A
class Prey:
    def flee(self):
        print("This animal is fleeing")

class Predator:
    def hunt(self):
        print("This animal is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Predator,Prey):
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.flee()
hawk.hunt()
fish.hunt()