# class method is used to create objects without creating an instance
"""
Uses of class method:
    1. making an object using files
    2. making an object using API, etc.
otherwise i have to call api outside the class and then pass the data as parameter
which will make it unorganised. Therefore, we use class methods.
"""

class Student:

    @classmethod
    def create_student_with_params(cls, name: str, age: int):
        # cls is the class whose instance we want to create i.e. Student
        student_object = cls(name, age)
        return student_object  # returning is important
    
    @classmethod
    def create_student_with_file(cls, filename):
        file = open(filename)
        data = file.read()
        name, age, gender = data.split()
        file.close()
        
        return cls(name, age, gender)


# creating an object without creating an instance
s1 = Student.create_student_with_params("aman", 20)

# creating an object with a file
s2 = Student.create_student_with_file('sample_text_file.txt')

