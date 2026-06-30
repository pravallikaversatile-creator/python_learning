#using ' and " to represent strings

variable1="Pravallika's python exercises"

#variable2='Pravallika's python exercises' #Here, we could not use ' and ' to enclose a string becoz, there is already a ' inside the string.

print(variable1)
print(type(variable1))

#print(variable2)

### Exercise 2 ###

variable1 = """Pravallika
is amazing"""
print(variable1)    #This is valid because triple quotes define a multi‑line string literal.
print(type(variable1))


### Exercise 3 ###

#   variable2 = 'Pravallika
#   is amazing'

#   print(variable2)    #a string enclosed in single quotes ' ' or double quotes " " cannot span multiple lines in Python.

#   print(type(variable2))

## Exercise 4 - Indexing in strings ##
a="Pravallika"
#Each charecter in string 'a' could be accessed using indexing. a[0]=P, a[1]=r, a[2]=a.....a[9]=a
for i in a:
    print(i,end=" ")
print("\n")
for i in range(len(a)): #len(a) gives length of string a
    print("i = ",i,"a[i]= ",a[i],sep=" ")
print("\n")
for i in range(len(a)):
    print(a[-i],end=" ") #negetive Indexing of string is aswell supported in Python.
print("\n")

### Exercise 5 String modification ###
variable="Pravallika"
# variable[2]="b" ## TypeError: 'str' object does not support item assignment
print(variable)
del(variable) # This deletes the variable

# print(variable) #NameError: name 'variable' is not defined.

### Exercise 6 String concatenation ###
n="Pravallika"
m="is amazing"
print(n+m) # Does not give space between two strings
print(n+" "+m) #Adds space between the strings

### Exercise 7 Finding letter in a string ###
variable3="Pravallika"
'z' in variable3
variable3="Pravallika"
print('z' in variable3) #Checking for letter z in the string
print('v' in variable3) #Checking for letter v in the string

### Exrecise 8 Using Escape sequences to seperate the string ###
print("Pravallika \nis an amazing girl \tshe loves coding in \vpython") 

### Exercise 9 Printing raw version of string ###
print("C:\newfolder\Downloads") #String gets corrupted because of \n in newfolder
print(r"C:\newfolder\Downloads") #String is preserved with r - Printing the raw version of a string is useful whenever you want Python to show the string exactly as written, without interpreting escape sequences like \n, \t, \v, \\, etc.

### Exercise 10 using format ###
name=input("Please enter your name: ")
print("Hi {}, How are you?".format(name))
age=input("Please enter age: ")
print("{} is {} years of age".format(name,age))

print("{} {}".format("Hello", "World"))

#.format() replaces {} placeholders in a string with values.
print("{} is {} years old".format("Pravallika", 20)) #Empty Placeholders usage
print("{0} scored {1} marks".format("Pravallika", 95)) #numbered placeholders
print("{name} lives in {city}".format(name="Pravallika", city="London")
) #Named Placeholders
print("{:.2f}".format(3.14159))   # 3.14 #Formatting Placeholder
print("{:05d}".format(42))        # 00042

print("{:<10}".format("Hi")) #left align
print("{:>10}".format("Hi")) #right align
print("{:^10}".format("Hi")) #center align

### Split function in python ###
words="a-b-c-d e"
print(words.split("-"))

### find ###
variable = "Pravallika is an amazing girl"
print(variable.find("amazing")) # If find is successful, it returns the starting index of the word in that string
print(variable.find("very")) #if find returns a negetive value, it means, it couldnot find the string

### Print the words in the string ###
variable=input("Enter a scentence: ").split()
print("Number of words in the string are: ",len(variable))
words=0
for i in variable:
    if i== " ":
        words+=1

print("Number of words in the string are: ",len(variable))

