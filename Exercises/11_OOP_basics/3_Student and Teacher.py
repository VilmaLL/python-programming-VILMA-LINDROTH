
class Student:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
    def study(self):
        print("study...study...study...more study")
    def say_hello(self):
        print(f"Yo, I am a student, my name is {self.name}, I am {self.age} years old, my email adress is {self.email}")

class Teacher:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email   
    def teach(self):
        print("teach...teach...teach...more teaching")
    def say_hello(self):
        print(f"Hi, my name is {self.name}, I am {self.age} years old, my email address is {self.email}")


teacher = Teacher("Pernilla", 32, "pernilla@gmail.com")
student = Student("Karl", 25, "karl@gmail.com")

print(teacher.teach())
print(teacher.say_hello())
print(student.study())
print(student.say_hello())