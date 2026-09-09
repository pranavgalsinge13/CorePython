# Function Decorators

# normal function ---> Decorator ---> Extended function

# @decor is used to call the decor function



'''def decor(func):
    def inner(name):
        if name=="Yash":
            print("Hello Yash Good Evening")
        else:
            func(name)
    return inner

@decor

def wish(name):
    print("Hello",name,"Good Morning")
wish("Pranav")
wish("Hitesh")
wish("Yash")

# without using @decor

def decor(func):
    def inner(name):
        if name=="Sunny":
            print("Hello Sunny Bad Morning")
        else:
            func(name)
    return inner

def wish(name):
    print("Hello",name,"Good Morning")

decorfunction=decor(wish)


wish("Durga")
wish("Sunny")
decorfunction("Durga")
decorfunction("Sunny")'''

def decor (func):
    def inner(a,b):
        c=int(input("Enter Third Number:"))
        func (a,b,c)
    return inner

@decor
def add(a,b,c):
   result=a+b+c
   print(result)
   return result


a=int(input("Enter First Number:"))
b=int(input("Enter Second Number:"))

add(a,b)
