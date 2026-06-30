Triple‑quoted strings are multi‑line string literals.
They can be assigned to a variable:
For Example:
text = """
Hello
World
"""

They can also be used as docstrings:
def greet():
    """
    This function prints a greeting.
    """
    print("Hello")

In this case, Python stores the string as the function’s __doc__.


"""
This looks like a comment,
but Python actually creates a string here.
"""
If this string is not assigned to a variable or used as a docstring, Python simply creates it and immediately discards it, but it still exists at runtime.

"""
This is a fake comment block.
Python ignores it because nothing uses the string.
"""
Python doesn’t error, so beginners assume it’s a comment.
But internally, Python still creates a string object, then throws it away.

