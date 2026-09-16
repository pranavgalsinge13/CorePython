# Object-oriented programming (OOP) organizes code using classes and objects.
#
# Key OOP concepts demonstrated below:
# - Class: a blueprint that defines data and behavior.
# - Object: an instance created from a class (s1 and s2).
# - Encapsulation: an object's data and methods are grouped together.
# - Constructor: __init__ initializes each object's attributes.
# - self: refers to the current object.
# - Method: display() defines behavior for Student objects.
# - Inheritance and polymorphism are other OOP concepts; they are not needed
#   in this basic example.

'''class student:
    def __init__(self):
        self.name='pranav'
        self.age=20
        self.marks=80

    def display(self):
        print("Hello I am:",self.name)
        print("My Age is:",self.age)
        print("My Marks are:",self.marks)


s1=student()
s1.display()'''


class student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks

    def display(self):
        print("Name of the student is:",self.name)
        print("Age of the student is:",self.age)
        print("Marks of the student is:",self.marks)


s1=student("Pranav",20,90)
s2=student("Yash",23,95)
s1.display()
s2.display()

