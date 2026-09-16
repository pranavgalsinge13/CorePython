# Polymorphism

# Polymorphism means "many forms": the same operation can work with
# different types of objects, producing behavior appropriate to each type.

#  Types of polymorphism in Python:

# 1. Duck typing: objects need only provide the required method.
# 2. Operator overloading: the same operator can have different meanings based on the context.
# 3. Method overloading: the same method name can have different implementations
# based on the number or type of arguments.
# 4. Method overriding: a subclass can provide a specific implementation of a method
# that is already defined in its superclass.
# 5. constructor overloading: a class can have multiple constructors with different parameters.


# method overloading

# example of method overloading in Python:

'''class test:
    def wish(self):
        print("Hello")

    def wish(self,a):
        print("Hello Jii")

    def wish(self,a,b):
        print("Hello Jii kya haal chal")

t=test()
# t.wish()
# t.wish(10)
t.wish(10,20)

# demo program with default arguments:

class test:
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print("The sum of three numbers is:",a+b+c)
        elif a!=None and b!=None:
            print("The sum of two numbers is:",a+b)
        else:
            print("Please provide at least two numbers to calculate the sum.")

t=test()
t.sum(10,20,30)
t.sum(10,20)

# demo program with variable length arguments:

class test:
    def sum(self,*a):
        total=0
        for i in a:
            total+=i
        print("The sum is:",total)

t=test()
t.sum(10,20,30)

# method overriding

# demo program of method overriding in Python:

class P:
    def property(self):
        print('Gold+Land+Cash+Power')
    def marry(self):
        print('Appalamma')
class C(P):
    def marry(self):
        print('Katrina Kaif')

c=C()
c.property()
c.marry()

# from overriding method of child class, we can call parent class method using super() function:

class P:
    def property(self):
        print('Gold+Land+Cash+Power')
    def marry(self):
        print('Shraddha Kapoor')
class C(P):
    def marry(self):
        super().marry()
        print('Alia Bhatt')

c=C()
c.property()
c.marry()'''

# constructor overriding
#
# Constructor overriding occurs when a child class defines its own __init__()
# method instead of using the parent class's constructor. The child constructor
# can initialize its additional attributes and call super().__init__() to reuse
# the parent constructor's initialization. Here, Person initializes name and
# age, while Employee adds eno and esal.

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class Employee(Person):
    def __init__(self,name,age,eno,esal):
        super().__init__(name,age)
        self.eno=eno
        self.esal=esal

    def display(self):
        print("Employee Name:",self.name)
        print("Employee Age:",self.age)
        print("Employee Number:",self.eno)
        print("Employee Salary:",self.esal)

e1=Employee('Pranav',20,101,50000)
e1.display()

e2=Employee('Yash',23,102,60000)
e2.display()