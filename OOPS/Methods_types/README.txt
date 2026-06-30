⭐ Types of Methods in Python
Python supports three main types of methods inside a class:

Instance Methods

Class Methods

Static Methods

These differ based on how they access data and how they are called.

⭐ Summary Table (Perfect for Notes)

Method Type	First Parameter	Access Instance Data	Access Class Data	Decorator	Use Case
_________________________________________________________________________________________________________________________________________
Instance Method		self		✔ Yes			✔ Yes		None		Work with object data
Class Method		cls		✘ No			✔ Yes		@classmethod	Modify class attributes, alternative constructors
Static Method		None		✘ No			✘ No		@staticmethod	Utility/helper functions


