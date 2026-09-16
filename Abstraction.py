# Abstraction means hiding implementation details and exposing only the essential functionality.


from abc import ABC, abstractmethod


class Car(ABC):
	@abstractmethod
	def speed(self):
          pass

class BMW(Car):
    def speed(self):
        print("BMW can run at 200km/hr")

class Audi(Car):
    def speed(self):
        print("Audi can run at 250km/hr")

class mercedes(Car):
    def speed(self):
         print("Mercedes can run at 300km/hr")

b= BMW()
b.speed()

a= Audi()
a.speed()

m= mercedes()
m.speed()



