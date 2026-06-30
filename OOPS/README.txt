⭐ Object-Oriented Programming (OOP) in Python
Object-Oriented Programming is a style of programming where we model real‑world entities using classes and objects.

It helps you write code that is:

Reusable

Organized

Secure

Easy to maintain

⭐ Why OOP?
Real‑world things have:

Properties (data)

Functionalities (actions)

Example: A Car

Properties → mileage, fuel type, seating capacity

Functionalities → start, stop, accelerate, brake

In Python:

Variables represent properties

Functions represent functionalities

OOP allows us to combine both inside a single structure called a class.

⭐ Class vs Object (The Heart of OOP)
Class
A class is a blueprint or template.

It defines:

What properties an object will have

What actions it can perform

Object
An object is a real instance created from the class.

Think of it like:

Class → Blueprint of a car

Object → Actual car (BMW, Kia, Benz, Range Rover)

⭐ Example: Car as a Class
Class (Blueprint)
Properties:

mileage

fuel_type

seating_capacity

Functionalities:

start()

stop()

accelerate()

Objects (Real Cars)
BMW

Kia

Range Rover

Benz

Each object has the same structure, but different values.

class Car:
    def __init__(self, brand, mileage, fuel_type):
        self.brand = brand
        self.mileage = mileage
        self.fuel_type = fuel_type

    def start(self):
        print(self.brand, "is starting")

    def stop(self):
        print(self.brand, "is stopping")


# Creating objects
car1 = Car("BMW", 15, "Petrol")
car2 = Car("Kia", 18, "Diesel")

car1.start()
car2.stop()

⭐ Why OOP Is Powerful
You can create multiple objects from the same class

Code becomes modular

You avoid repetition

You can secure data using encapsulation

You can extend functionality using inheritance

You can reuse code using polymorphism

Python uses self (explicit) and C++ uses this (implicit) to refer to the current object.
Both serve the same purpose: accessing object attributes and methods.
