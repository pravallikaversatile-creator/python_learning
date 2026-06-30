Data types like int, float, string,complex and Boolean are Primitive data types.
List and Tuple
Set and Dictionaries are also data types.
These are collection based data types.
In a list, we can store a collection of int variables, collection of float variables, collection of strings, complex variables, boolean variables, a list itself or it can be a collection which is a mix of these all.
List, Tuple, set and dictionary differ in 4 different properties
- Ordered or not
- Indexed or not
- mutable or not
- duplicate or not allowed
example d=[1,2,3.5,"Pravallika"] --- its a list
	e=(1,2,3.5,"Pravallika") --- its a tuple

	List			Tuple
       ______		       _______
       Ordered			Ordered
       Indexed			Indexed
       Mutable			Not Mutable
       Allows Duplicate		Allows Duplicate

Ordered: ex:[1,2,3.5,"pravz"] --- Ordered means the elements keep the same sequence in memory and iteration.
Python preserves insertion order for all sequence types (list, tuple, string).
Indexed: Indexed means each element has a fixed position (0, 1, 2, …).
Any ordered sequence (list, tuple, string) is automatically indexed.
Mutable: Mutable means you can change, add, remove, or replace elements after creation. a = [1, 2, 3]
a[0] = 10
Not Mutable (Tuple)
t = (1, 2, 3)
t[0] = 10   # ❌ Error
Lists and tuples allow duplicates because Python does not enforce uniqueness.
Duplicate values may or may not share memory depending on Python’s internal optimization
[1, 1, 1]
(2, 2, 2)

Use a list when you want something that can change.
Use a tuple when you want something that must stay fixed.
When to use a List
Use a list when:

You need to add, remove, or modify items

The data is dynamic

Order matters

You want to sort or rearrange items

You need a container for loops, building collections, or user input

✔ Examples where a list is the right choice
A shopping cart that changes

A list of student marks

A list you append to inside a loop

A list of files in a folder

A list of user inputs
marks = [90, 85, 88]
marks.append(92)

When to use a Tuple
Use a tuple when:

The data must not change

You want to protect the values

You want to use the data as a dictionary key

You want faster performance than a list

The data represents one complete item (record‑like)
point = (10, 20)
today = (2026, 6, 10)

