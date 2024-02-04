class Student:
    # called as attributes
    name = "aman"
    roll_no = 10

    # methods
    def info(self):  # self is imp and indicates the object
        print(f"{self.name}'s fees is paid")

    def abc(self):
        self.school = "xyz"  # creates an attr school

    # params
    def change_name(self, new_name: str):
        self.name = new_name


# creates an object
s1 = Student()

# an object can't be printed
print(s1)  # gives address in the memory

# attributes can be printed
print(s1.name)

# attributes can be modified
s2 = Student()
s2.name = "Goku"
s1.info()

print(s2.name)
