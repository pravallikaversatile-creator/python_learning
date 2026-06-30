Set and Dictionaries are collection based data types aswell, which are used to group and store various other data types.
	Sets						Dictionaries
       __________________________________________________________________________________________________________________________________________________________
       Un Ordered					Ordered (Python version 3.6 and earlier, Dictionaries were unordered.From Version 3.7, they are Ordered.)
       UnIndexed					Indexed
       Set as whole is
       Mutable, but Set elements are not		Mutable
       Duplication not allowed				Duplication not allowed

set elements must be immutable
(e.g., numbers, strings, tuples)

But the set itself IS mutable.

So:

You can modify the set

You cannot modify the elements inside it (if they are immutable types)

s = {1, 2, 3}
s.add(4) # This works
print(s)
s.remove(2) #Works
print(s)
s.update([5, 6]) #works
print(s)
fs = frozenset([1, 2, 3])
fs.add(4)   # ❌ Error

✔ Set
add() → add ONE

update() → add MANY

✔ List
append() → add ONE at END

insert() → add ONE at POSITION

extend() → add MANY at END

A dictionary is a mutable, unordered, key–value data structure.
Data storage is like this: key : value
student = {"name": "Pravz", "age": 12, "marks": 95}

⭐ Most Important Set Methods
Sets are all about unique items, no indexing, and fast membership checks.

🔹 Adding & Removing Elements
add — adds a single element

update — adds multiple elements

remove — removes an element (errors if missing)

discard — removes an element (no error if missing)

pop — removes and returns a random element

clear — empties the set

🔹 Set Operations (VERY important)
union — combine sets (A ∪ B)

intersection — common elements (A ∩ B)

difference — elements in A not in B (A − B)

symmetric_difference — elements not common to both

⭐ Most Important Dictionary Methods

🔹 Accessing Keys, Values, Items
keys — returns all keys

values — returns all values

items — returns key–value pairs

🔹 Adding & Updating
update — add/update multiple key–value pairs

🔹 Removing Items
pop — remove by key, return value

popitem — remove last inserted pair

clear — empty the dictionary
