"""Create a class named Person with a string variable 'name' and an integer variable 'age,' such that these variables are not accessible outside the class and implement a way to initialize the variables and print the variables.

Functions: 1.setValue- that sets the variables value. 2.getValue- that prints the variables value."""

class Person:
    def setValue(self,name,age):
        self.name=name
        self.age=age

    def getValue(self):
        print("{} is {} years old".format(self.name,self.age))


p=Person() #Creating Objcet p for class Person
name,age=input("Enter name and age of sperson seperated by space: ").split()
age=int(age)
p.setValue(name,age)
p.getValue()
