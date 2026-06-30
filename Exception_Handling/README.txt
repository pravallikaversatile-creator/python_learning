Exception Handling lets the program deal with errors without crashing.
It basically gives a structure to "try something risky" and "handle what goes wrong"

The Core Structure
******************
try:
	#risky code
except SomeError:
	#What to do if the error happens
else:
	#runs if NO error happens
finally:
	#always runs (error or no error)

⭐ Why We Use Exception Handling
********************************
To prevent program crashes

To show user‑friendly messages

To handle unexpected input

To continue running even after an error

⭐ Most Common Exceptions (You’ll see these often)
**************************************************
ZeroDivisionError — dividing by zero

ValueError — wrong type of input

TypeError — wrong data type

IndexError — list index out of range

KeyError — missing dictionary key

FileNotFoundError — file doesn’t exist
