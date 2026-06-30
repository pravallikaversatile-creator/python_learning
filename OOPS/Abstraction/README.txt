Abstraction is hiding of unnecessary details.
How is Abstraction implemented in Python?
Abstract classes and Abstract Methods
Unlike Java, Pythons don't support Abstract classes and Abstarct Methods. We kind of bring it into Python using the concept of Modules.
class Vehicle - In real world, there will be no vehicles, but we have cars, bycycles, Aeroplanes etc, so an object for vehicle should not really be called, as objects in python are real world entities.
So Vehicle is considered as an Abstract class and the methods implemented inside it like start, stop... etc are considered as Abstract methods.
An abstract class is a class that cannot be instantiated.
It exists only to be inherited.

We create it using:

from abc import ABC, abstractmethod
✔ Purpose
Define a common interface

Force child classes to implement certain methods

Provide partial implementation

⭐ What is an Abstract Method?
An abstract method is a method declared in the base class but must be implemented in the child class.
@abstractmethod
def method_name(self):
    pass
If a child class does not implement it → Python throws an error.

The uniqueness of the ABC module (Abstract Base Classes) in Python is that it gives Python a formal, enforceable way to define interfaces and enforce method implementation, even though Python is a dynamically‑typed language.
Without ABC, Python can't force child classes to implement required methods.

⭐ Core Idea
An abstract class is valuable not because it contains code, but because it defines what MUST exist in every child class.

It enforces a contract.

Even if the abstract class has no implementation, it tells all subclasses:

“You MUST implement these methods.”
