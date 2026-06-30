"""
#Exercise 1
l=[1,2,3,4,5,6]
i=int(input("Enter index of element to be printed: "))
print(f"Element at index {i} is: {l[i]}")
d=int(input("Enter by which number should the index element be divided: "))
up=int(l[i]/d)
print(f"Element at index {i} after division with d is : {up}")
l[i]=up
print(f"Final list is {l}")

"""
"""

#Exercise 2 with Exceptions Handling
l=[1,2,3,4,5,6]
try:
    i=int(input("Enter index of element to be printed: "))
    print(f"Element at index {i} is: {l[i]}")
    d=int(input("Enter by which number should the index element be divided: "))
    up=int(l[i]/d)
    print(f"Element at index {i} after division with d is : {up}")
    l[i]=up
    print(f"Final list is {l}")
except ValueError:
    print("Please enter valid number")
except IndexError:
    print("Please enter valid Index")
except ZeroDivisionError:
    print("Division by Zero is not allowed")
except Exception as e:
    print(f"unexpected Error {e}")
"""

#Exercise 3 with Exceptions Handling and using Finally.
try:
    operand1,operand2=map(int,input("Enter two numbers seperated by space: ").split())
    operator=input("choose an operator between '+,-,*and/' ")
    if operator == "+":
        result = operand1 + operand2
    elif operator == "-":
        result = operand1 - operand2
    elif operator == "*":
        result = operand1 * operand2
    elif operator == "/":
        result = operand1 / operand2
    else:
        raise KeyError("Invalid Operator")
    print(f"Result of operation is: {result}")
except ValueError:
    print("Please enter valid operands")
except ZeroDivisionError:
    print("Division by Zero is not allowed")
except Exception as e:
    print(f"unexpected Error {e}")
else: #Executes when control does not hit with any Exceptions.
    print("No Exceptions encountered")
finally: #Executes weather or not Control hits with any exception errors.
    print("Calculation Attempt Finished")
