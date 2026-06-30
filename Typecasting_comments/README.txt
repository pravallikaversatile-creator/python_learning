a=3 
b=3.14 
c='Pravz'

when 3 is asigned to a, 3.14 to b and pravz to c, a is implicitly type converted to hold an interger, b is implicitly type casted to float and c is implicitly type casted to a string.

Explicit type casting means you manually convert a value from one data type to another using functions like int(), float(), str(), bool(), etc.

An explicit type cast succeeds only if the source value can be meaningfully represented in the target type. Otherwise, Python raises an exception (usually ValueError or TypeError).

repr() stands for representation.

It returns the official string representation of an object — a version that is intended to show exactly what the object is, often including quotes for strings.

Commenting
For single line comments use #

# This is a comment

a = 10  # This is also a comment
print(a)

for Multiple-line comments use # for each line

# This is line 1
# This is line 2
# This is line 3

	or

Triple quoted strings

"""
This is a multi-line
string.
It is sometimes used like a comment.
"""
