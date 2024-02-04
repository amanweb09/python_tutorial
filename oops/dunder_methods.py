# some special methods
# eg. __init__, __str__, etc

class Bank:

    # initializes the object
    def __init__(self) -> None:
        self.name = input("Enter name ")
        self.balance = 0

    # runs when you try to print the object 
    # by default __str__returns the hexadecimal address of the object in the memory
    def __str__(self) -> str:
        return f"Your name is {self.name} and balance is {self.balance}"


my_acc = Bank()
print(my_acc)