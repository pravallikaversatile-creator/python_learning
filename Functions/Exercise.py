

#Simple Function
def sayHello():
    print("Inside the Function Definition: Hello")
    print("Inside the Function Definition: Hope Everything is Good!")

print("Calling the Function")
sayHello()

#Function with passing arguments
def addition(a,b):
    print("Inside the Function Definition, sum is: ",a+b)

print("Calling the Function")
addition(3,5)

#Function with return Value
def subtraction(u,v):
    print("Inside function returning the value ")
    return u-v

print("Function call, Difference is: ",subtraction(8,3))

#Example 5 
def data_transfer(a):
    a+=5
    return (a)

#Driver code
#print("In Driver code, calling Function data_transfer(), value of a: ",data_transfer(5))
a=5
print("In Driver code, calling Function data_transfer(), value of a: ")
data_transfer(a)
print("value of a is: ",a)

#Exercise Print Divisors of a number - Method 1
def find_Divisors(in_value):
    print("The Divisors of the number are: ")
    for i in range (1,in_value+1):
        if(in_value % i == 0):
            print(i,end=" ")

in_value=int(input("Enter the value to find Divisors: "))
find_Divisors(in_value)
print(end="\n")


#Exercise Print Divisors of a number - Method 2
def find_Divisors(in_value):
    divisor_list=[]
    for i in range (1,in_value+1):
        if(in_value % i == 0):
            divisor_list.append(i)
    return divisor_list

in_value=int(input("Enter the value to find Divisors: "))
print("The List of Divisors are : ",find_Divisors(in_value))


#Exercise Print Divisors of a number - Method 3
def find_Divisors(in_value):
    divisor_list=[]
    for i in range (1,in_value+1):
        if(in_value % i == 0):
            divisor_list.append(i)
    return tuple(divisor_list)

in_value=int(input("Enter the value to find Divisors: "))
print("The List of Divisors are : ",find_Divisors(in_value))



#Merging Dictionaries
def create_dict():
    dict1 = {}
    items=int(input("Input number of Keys: "))
    for i in range (0,items):
        key=input("Enter key: ")
        value=input("Enter value: ")
        dict1[key]=value
    return dict1

print("Calling create_dict function to create a Dictionary: ")
my_dict1=create_dict()
print("Created the first Dictionary. Dictionary 1 is: ",my_dict1)
print("Calling create_dict function to create a second Dictionary: ")
my_dict2=create_dict()
print("Created the second Dictionary. Dictionary 2 is: ",my_dict2)

