# Inheritance
#
# Inheritance lets a child (derived) class reuse and extend the attributes
# and methods of a parent (base) class. It represents an "is-a" relationship.
#
# Syntax:
# class Child(Parent):
#     pass
#
# A child class automatically receives accessible members from its parent and
# can add new methods or override inherited methods. Python also supports
# single, multilevel, multiple, hierarchical, and hybrid inheritance.

# - Code reusability
# - create a new class child calss (derived class) using existing class (parent class, base class)
# - child class acquires all the properties of parent class
# - follow Is A Relationship

# example
# python single level inheritance

'''class Animal:
    def speak(self):
        print("Animal Speaking")
# child class Dog inherits the base class Animal

class Dog(Animal):
    def bark(self):
        print("dog barking")
d=Dog()
d.bark()
d.speak()

# Python multi-level inheritance
# example 2 

class Animal:
    def speak(self):
        print("Animal Speaking")

# The child class Dog inherits the base class Animal

class Dog(Animal):
    def bark(self):
        print("dog barking")

# the child class Dogchild inherits another child class Dog

class DogChild(Dog):
    def eat(self):
        print("Eating bread...")

d=DogChild()
d.bark()
d.speak()
d.eat



# python multiple inheritance

class Calculation1:
    def Summation(self,a,b):
        return a+b;

class Calculation2:
    def Multiplication(self,a,b):
        return a*b;

class Derived(Calculation1,Calculation2):
    def Divide(self,a,b):
        return a/b;

d=Derived()

print(d.Summation(10,20))
print(d.Multiplication(10,20))
print(d.Divide(10,20))'''



# Python Hierarchical inheritance 

class Animal:
    def eat(self):
        print("Animal can eat")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Cat(Animal):
    def meow(self):
        print("Cat meows")

d=Dog()
d.eat()
d.bark()

c=Cat()
c.eat()
c.meow()


# Python Hybrid inheritance
# Hybrid inheritance is a combination of more than one type of inheritance.
# Example: Pet inherits from both Dog and Cat, and both Dog and Cat inherit from Animal.

class Animal:
    def eat(self):
        print("Animal eats")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Cat(Animal):
    def meow(self):
        print("Cat meows")

class Pet(Dog, Cat):
    def play(self):
        print("Pet plays")

p = Pet()

p.eat()      # inherited from Animal
p.bark()     # inherited from Dog
p.meow()     # inherited from Cat
p.play()     # defined in Pet