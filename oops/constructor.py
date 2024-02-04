class Student:
    # calls automatically as an object is formed
    def __init__(self, school):
        self.name = input("Enter name -->")
        self.age = input("Enter age --> ")
        self.school = school

s1 = Student("DPS")