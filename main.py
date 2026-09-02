import test_module;
name=input("what is your name?")
test_module.show(name)

# Variables in Module

import test_module;
a=test_module.Person1["age"]
print(a)

# from import

from calculation import addition

a=int(input("Enter a"))
b=int(input("Enter b"))

print("Addition=",addition(ab))