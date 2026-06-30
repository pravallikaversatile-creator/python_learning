#Exercise to import mymodule and reuse it in import_mymodule.py file using import
import mymodule
import math
import math as m

mymodule.greet("Pravallika")
print(f"Square Root of 256 is {math.sqrt(256)}") #Imported the whole module
print(f"Square Root of 196 is {m.sqrt(196)}") #Imported as alias
print(f"Listing the contents of math module {dir(math)}")
