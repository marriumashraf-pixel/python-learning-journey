class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")
stud1 = Student("mimi", 21)
stud1.display()
stud2 = Student("ali", 23)
stud2.display()