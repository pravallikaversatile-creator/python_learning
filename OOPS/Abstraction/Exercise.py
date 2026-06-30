#Implementing an Abstract class
import abc
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
class car(Vehicle):
    def Horn(self):
        print("Horning")
    def start(self):
        print("Starting")
C1=car()
C1.Horn()
C1.start()

print(f"Listing abc module contents: {dir(abc)}") #Lists the contents of abc module

#One more Example for Abstract Classes

import abc
from abc import ABC, abstractmethod

class Animal(ABC):
    
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
       return "Barks"


class Lion(Animal):
    def sound(self):
       return "Roars"


class Orangutan(Animal):
    def sound(self):
       return "Howls"

D1=Dog()
print(f"Dog {D1.sound()}")
L1=Lion()
print(f"Lion {L1.sound()}")
O1=Orangutan()
print(f"Orangutan {O1.sound()}")
