# encapsulation
# Encapsulation means restricting direct access to data and using methods
# to control how it is read or modified.

'''class Fortune:

    __wifi=""
    contact=0

    def __init__(self):
        self.__wifi="ghe re fukatach aahe"   #private variable
        self.contact= 1234567890           #public variable

        print(self.__wifi)
        print(self.contact)

f= Fortune()'''

# protected variable
# A protected variable is one whose name starts with a single underscore (_).
# It is meant to be accessed only within the class and its subclasses.
# Python does not enforce strict protection, but it follows a convention.

'''class Parent:
    def __init__(self):
        self._money = 5000   # protected variable

class child(Parent):
    def display(self):
        print(self._money)   # child class can access protected member

c = child()
c.display()'''

# Output:
# 5000
# Here, _money is protected because only subclasses can use it.
# Outside the class, it should be accessed carefully to avoid direct changes.


# private variable
# A private variable is one whose name starts with a double underscore (__).
# It is meant to be accessed only within the class and is not accessible from outside the class or its subclasses
# Python uses name mangling to make private variables less accessible from outside the class.
# if we declare any variable or method as private, then it can be accessed only within the class 
# and not from outside the class or its subclasses.


class Rectangle:
    __length = 0  # private variable
    __breadth = 0  # private variable

    def __init__(self): #constructor
        self.__length = 5
        self.__breadth = 3

        print(self.__length)
        print(self.__breadth)

rec=Rectangle()
print(rec.__length)  # This will raise an AttributeError because __length is private
print(rec.__breadth)  # This will also raise an AttributeError because __breadth is private 
