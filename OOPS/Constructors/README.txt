⭐ Constructors in Python (Brief & Clear)
A constructor is a special method that runs automatically when an object is created.

✔ Name of constructor in Python
__init__() → a dunder (double‑underscore) method.

✔ Purpose
Initialize object properties

Allocate memory

Set default values

Example
class Car:
    def __init__(self, brand, mileage):
        self.brand = brand
        self.mileage = mileage
c = Car("BMW", 15) #When this object is created
Car.__init__(c, "BMW", 15) #Python automatically calls this dunder method


Dunder methods allow Python objects to behave like built‑in types.
__init__(self, ...) #Constructor — initializes object properties.
__str__(self)	    #Returns a human‑readable string when you print the object.
__repr__(self)      #Developer‑friendly representation of the object.
__len__(self)       #Defines behavior for len(object).
__add__(self, other) #Defines behavior for object1 + object2.
__eq__(self, other)  #Defines behavior for object1 == object2
__del__(self)        #Destructor — called when object is deleted.

Default constructor → no parameters, used for fixed initialization.

Parameterised constructor → takes parameters, used for dynamic initialization.

