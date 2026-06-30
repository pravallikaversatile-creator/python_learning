
#Exploring Class and Instance Attributes
class Person:
    place="London"
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def getValue(self):
        print("In getValue: {} is {} years old and lives in {}".format(self.name,self.age,Person.place))


name,age=input("Enter name and age of a person1 seperated by space: ").split()
age=int(age)
p1=Person(name,age) #Creating Objcet p for class Person
p1.getValue()
print("Outside class: {} is {} years old and lives in {}".format(p1.name,p1.age,p1.place))


name,age=input("Enter name and age of a person2 seperated by space: ").split()
age=int(age)
p2=Person(name,age) #Creating Objcet p for class Person
p2.getValue()
print("Outside class: {} is {} years old and lives in {}".format(p2.name,p2.age,p2.place))



name,age=input("Enter name and age of a person3 seperated by space: ").split()
age=int(age)
p3=Person(name,age) #Creating Objcet p for class Person
p3.getValue()
print("Outside class: {} is {} years old and lives in {}".format(p3.name,p3.age,p3.place))


#Example-2

class car:
    def __init__(self):
        self.name="Tesla"
        self.milage=300
        print("Inside init name is {} and milage is {}.".format(self.name,self.milage))
    def get_value(self):
        print("Inside get_value method: name is {} and milage is {}.".format(self.name,self.milage))

c1=car()
c1.name="EC40"
c1.milage=330
c1.get_value()
print("Outside class, First Object instance: c1 name is {} and milage is {}.".format(c1.name,c1.milage))

c1.name="Ex30"
c1.milage=250
c1.get_value()
print("Outside class, Second Object instance: c1 name is {} and milage is {}.".format(c1.name,c1.milage))

"""
⭐ Key Concept: Instance Attributes Are Mutable
The constructor gives default values, but Python allows you to modify them anytime:

Inside the class

Outside the class

After object creation

The constructor sets initial values for instance attributes.
But instance attributes can be modified anytime after object creation.
That’s why assigning c1.name = "EC40" overrides the constructor’s "Tesla".

"""
