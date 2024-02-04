# Extending a class

# PARENT CLASS
class Car:
    def __init__(self, wheels: int, seats: int, category: str = "LMV"):
        self.wheels = wheels
        self.seats = seats
        self.category = category


# CHILD CLASS
# Audi has all properties of Car with some additional properties
class Audi(Car):
    def __init__(self, model: str, color: str):

        # super is used to access parent class inside child class
        super().__init__(4, 5, "LMV")   
        
        self.model = model
        self.color = color


# only Audi init will run (an not Car init)
my_audi = Audi("A4", "white")


# can access properties of Car
my_audi.wheels = 4
my_audi.seats = 5


# Multiple inheritance
class Father:
    
    def printName(self) -> None:
        print("father")

class Mother():
    def print_m_name(self) -> None:
        print("mother")

# inherits both mother and father
class Child(Father, Mother):
    def __init__(self) -> None:
        # only father init will be called (jo pehle likha h)
        super().__init__()

    def print_m_name(self) -> None:
        print("child")
