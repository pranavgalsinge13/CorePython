# oops in python

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