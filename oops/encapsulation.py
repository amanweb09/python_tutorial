# restricting the access of class variables
# public, private, protected


class Student:
    name: str = "aman"
    ph_no: int = 987

    # making a private variable --> use __
    __database_id: str = "dps1456"

    def allot_roll_no(self) -> None:
        self.roll_no = 1234

    def change_db(self):
        # can be accessed inside the class but not outside it
        self.__database_id = "dpsxyz"

    # getter as we can call it to print the private vars
    def print_db_id(self) -> None:
        print(self.__database_id)

    # setter
    def set_db_id(self, new_id: str):
        self.__database_id = new_id


s1 = Student()

# public  --> can be accessed by the object
s1.allot_roll_no()
s1.name

# ----------------------

# private --> cant be modified and accessed by the object
# used when we dont want user to change it
s1.__database_id = "456"  # this will not change
# print(s1.__database_id) #error

# Getter --> used to print or access private vars
# we will make a function inside the class as private vars can only be accessed inside the class
s1.print_db_id()

# Setter --> to modify a private var
# we will make a function inside the class as private vars can only be accessed inside the class
s1.set_db_id("dps876")

# Accessing private vars --> object._className__variableName
# This is called name mangling
s1._Student__database_id    #NEVER DO THIS
# NOTE: This means private vars are not strictly followed

# ---------------------

# Protected --> Can be accessed by child class but not by the object
# called as access modifiers and created by one underscore _
class Father:

    # protected var
    _balance = 5000

    def __init__(self) -> None:
        self.father_name = input("Enter father's name ")
        self.father_phn = input("Enter father's phone number ")

class Child(Father):
    def __init__(self) -> None:
        super().__init__()
        self.child_name = input("Enter child's name ")
        # _balance can be accessed by the child
        self.balance = self._balance * 0.1