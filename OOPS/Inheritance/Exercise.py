"""Single Inheritance"""

class Automobile:
    def use(self):
        print("They are used to travel from one place to another")
class Car(Automobile):
    def Type(self):
        print("It can be Hybrid, Manual or Automatic")

vehicle=Car()
vehicle.use()
vehicle.Type()

A=Automobile()
A.use()
# A.Type() #This gives an Error

"""Multiple Inheritance"""

class Father:
    def Hobbies(self):
        print("Loves Coding in Python")
class Mother:
    def Interests(self):
        print("Loves coding in System Verilog")
class child(Father, Mother):
    def Likes(self):
        print("Loves coding in System Verilog and Python")
C1=child()
C1.Hobbies()
C1.Interests()
C1.Likes()

"""Multi Level Inheritance"""
class Automobile:
    def use(self):
        print("They are used to travel from one place to another")
class Car(Automobile):
    def Type(self):
        print("It can be Hybrid, Manual or Automatic")
class Benz(Car):
    def Security_System(self):
        print("Security System is Drive Authorization System")
vehicle=Car()
vehicle.use()
vehicle.Type()

BMW_3 = Benz()
BMW_3.Security_System()
BMW_3.Type()
BMW_3.use()

"""Hierarchial Inheritance"""
class shape:
    def properties(self):
        print("This can be 2D or 3D")
class Triangle(shape):
    def features(self):
        print("This is 2D")
class Sphere(shape):
    def properties(self):
        print("This is 3D")
sh1=shape()
Tr1=Triangle()
Sp1=Sphere()
sh1.properties()
Tr1.features()
Sp1.properties()

"""Hybrid Inheritance"""
class Grandfather:
    def profession(self):
        print("Interested in Farming")
class Father(Grandfather):
    def Hobbies(self):
        print("Loves Coding in Python")
class Mother:
    def Interests(self):
        print("Loves coding in System Verilog")
class child(Father, Mother):
    def Likes(self):
        print("Loves coding in System Verilog and Python")
GF1=Grandfather()
F1=Father()
M1=Mother()
C1=child()
C1.profession()

""" Built-in Function Super() in Python """
class Parent:
    def __init__(self):
        print("This is the Parent Class" )
class child(Parent):
    def __init__(self):
        super().__init__()
        print("This is Child's class")
P1=Parent()
C1=child()


""" Built-in Function Super() in Python """
class Parent:
    def info1(self):
        print("This is the Parent Class" )
class child(Parent):
    def info2(self):
        super().info1()
        print("This is Child's class")
P1=Parent()
C1=child()
C1.info2()


""" Built-in Function Super() Example-2 in Python """
class A:
    def test1(self):
        print("method named test1 of A called")
class B(A):
    def test1(self):
        print("method named test1 of B called")
        super().test1()  
class C(A):
    def test1(self):
        print("method named test1 of C called")
        super().test1()
class D(B,C):
    def test2(self):
        print("method named test2 of D called") 
object1 = D()
object1.test1()


""" Built-in Function Super() Example-3 in Python """

print("This is a new Example for Super() built-in function")
class A:
    def test1(self):
        print("method named test1 of A called")
class B(A):
    def test1(self):
        print("method named test1 of B called")
        super().test1()  
class C(A):
    def test1(self):
        print("method named test1 of C called")
        super().test1()
class D(B,C):
    def test1(self):
        print("method named test1 of D called") 
        super().test1()
#object1 = D()
#object1.test1()

object2= C()
object2.test1()

""" Problem statement
Create a Class Shape having a field shapeType and a function printMyType.

Create another class, Square and Rectangle, which inherits the Shape class and has additional fields length and breadth. Both Square and Rectangle classes will have two functions calculateArea, which will return the object's area, and printMyType, which will print the type of the object.

Inside the main, first create the object of class Square and have a length equal to 5 and call the printMyType then calculateArea method after creating the object of class Rectangle having the length equal to 5 and breadth equal to 4 and again call the printMyType and calculateArea method. """

class Shape:
    def __init__(self,shapeType):
        self.shapeType=shapeType
    def printMyType(self):
        print(self.shapeType)
class Square(Shape):
    def __init__(self,length):
        super().__init__("square")
        self.length=length
    def calculateArea(self):
        return self.length * self.length
class Rectangle(Shape):
    def __init__(self,length,breadth):
        super().__init__("rectangle")
        self.length=length
        self.breadth=breadth
    def calculateArea(self):
        return self.length * self.breadth
sq1=Square(5)
sq1.printMyType()
print(sq1.calculateArea())
rect1=Rectangle(5,4)
rect1.printMyType()
print(rect1.calculateArea())

#Example Vehicle Inheritance System
class Vehicle:
    def __init__(self,vehicleType):
        self.vehicleType = vehicleType
    def printMyType(self):
        print(self.vehicleType)
class Car(Vehicle):
    def __init__(self,brand,model):
        super().__init__("car")
        self.brand = brand
        self.model = model
    def getDetails(self):
        print(f"Brand is: {self.brand} and model is {self.model}")
class Bike(Vehicle):
    def __init__(self,brand,cc):
        super().__init__("Bike")
        self.brand = brand
        self.cc = cc

    def getDetails(self):
        print(f"Brand is: {self.brand} and engine capacity is {self.cc}")
C1=Car("Toyota","Corolla")
C1.printMyType()
C1.getDetails()
B1=Bike("Honda",150)
B1.printMyType()
B1.getDetails()

#Runtime polymorphism
class Shape:
    def render(self):
        print("Drawing a Generic shape")
class Circle(Shape):
    def render(self):
        print("Drawing a Circle")
class Rectangle(Shape):
    def render(self):
        print("Drawing a Rectangle")
class Triangle(Shape):
    def render(self):
        print("Drawing a Triangle")
def render(shapeObject):
    shapeObject.render()
C1=Circle()
R1=Rectangle()
T1=Triangle()

render(C1)
render(R1)
render(T1)

#Duck Typing Polymorphism
class Dog:
    def sound(self):
        return "Barking"
class Cat:
    def sound(self):
        return "Meow"
class Cow:
    def sound(self):
        return "Moo"
def makeSound(shapeObject):
    print(shapeObject.sound())
D1=Dog()
C1=Cat()
Co1=Cow()

makeSound(D1)
makeSound(C1)
makeSound(Co1)
