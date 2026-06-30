#Using parametrised __init__
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("Type of age is in init: ",type(age))

    def getValue(self):
        print("{} is {} years old".format(self.name,self.age))
        print("Type of age is in get_value: ",type(age))


name,age=input("Enter name and age of a person seperated by space: ").split()
age=int(age)
p=Person(name,age) #Creating Objcet p for class Person
p.getValue()


