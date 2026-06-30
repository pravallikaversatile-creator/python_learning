a=3
b=3.14
c=7.85
f=35
print(type(a))
print(type(b))
print(type(c))
e=str(f)
print(e)
print(repr(e))
print(type(e))


# This is a bit different scenario (string * integer)

a='pravz'
b=2
c=a*b
print(c)
print("This string * integer scenario")
print(type(c))

"""
d=a+str(b)
print(d)
print(type(d))

"""

# This is a bit different scenario (integer * string)

a=6
b="is amazing"
c=a*b
print("This integer * integer scenario")
print(c,sep=" ")#The sep parameter does not help to insert spaces here because, it is only used between multiple arguments passed to print(). 
print(type(c)) 

#sep operator working between multiple arguments
print("Hello", "World", sep=" "), #For example here, Hello and world are two different arguments, so seperator operator works.


#This is (string + string)
a="pravallika"
b="is amazing"
print(a+b,sep=" ")#The sep parameter does not help to insert spaces here because, it is only used between multiple arguments passed to print().
print(type(c))

#This is string + integer 
a="pravz"
b=5

"""
d=a+b #TypeError: can only concatenate str (not "int") to str, This causes an error because Python cannot concatenate a string and an integer directly.

print("This is when string is added to integer")
print(d)
print(type(d))

"""
d=a+str(b)
print("This is when integer is typecasted to string and added to string")
print(d) #since b is typecasted to string, d becomes a concatenation of strings and b.
print(type(d))

#Taking inputs Example
a=input("Please enter first number")
b=input("Please enter second number")
c=a+b
print("sum is",sep=" ")
print(c)
print(type(c))
