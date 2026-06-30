⭐ Difference Between Instance Attributes and Class Attributes
Instance attributes and class attributes are two different ways of storing data inside a class.
They differ in where they are stored, how they are accessed, and how many copies exist.

⭐ 1. Instance Attributes
Instance attributes 
	belong to each object individually. 
	Defined in __init__() using self.
	Stored in Object Memory.
	Have Copies of One per object.
	Whose Changes affect Only to that object.
	Example: self.name, self.age

⭐ 2. Class Attributes
Class attributes 
	belong to the class itself, not to individual objects.
	Defined Inside class, outside methods
        Stored in Class memory.
        Have One shared copy.
        Whose Changes effect All objects.
        Example: wheels = 4.

⭐ Example Showing Both
class Car:
    wheels = 4   # class attribute

    def __init__(self, brand):
        self.brand = brand   # instance attribute

c1 = Car("BMW")
c2 = Car("Kia")

print(c1.brand, c1.wheels)   # BMW 4
print(c2.brand, c2.wheels)   # Kia 4


