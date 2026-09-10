# oops in python

class student:
    def __init__(self):
        self.name='pranav'
        self.age=20
        self.marks=80

    def display(self):
        print("Hello I am:",self.name)
        print("My Age is:",self.age)
        print("My Marks are:",self.marks)


s1=student()
s1.display()