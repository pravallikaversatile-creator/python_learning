""" Working out Sets and Dictionaries """
# Example 1
Ex_Set={1,3.5,7+8J,"Pravz"}#We can see that order is not maintained
print("Printing a Set: ",Ex_Set)
print(type(Ex_Set))

#Example 2
## Ex_Set[3] = 4+9J #This gives Type error because set Elements are not mutable
print("Length of the set is : ",len(Ex_Set)) # Gives length of the set

#Example 3 For loop
print("Elements of the Set are: ")
for i in Ex_Set:
    print(i,end="\t")

print(end="\n")

#Example 4 Add elements in the Set
Ex_Set.add("intersting")
print("Elements of the Set are: ",Ex_Set)

#Example 5 Removing elements in the Set
Ex_Set.remove(7+8j)
print("Elements of the Set after removing 7+8j: ",Ex_Set)

# Example 6 Dictionaries
Ex_Dict = {"name":"Pravz","age":10,"Hobbies":["Learning","travelling","exploring"],"Marks1":8,"Marks2":6}
print("Printing the contents of the Dictionary: ",Ex_Dict)
print("Type of Ex_Dict is: ",type(Ex_Dict))
print("Extracting Hobbies value: ",Ex_Dict.get("Hobbies") ) #Ex_Dict.get("Key") gives the value of that key
Ex_Dict_keys=Ex_Dict.keys()
print("Extracting all the keys of the Dictionary: ",Ex_Dict.keys()) #Ex_Dict.keys() gives list of all the keys
print("Extracting values through the keys of the Dictionary: ") #Ex_Dict.keys() gives list of all the keys
for i in Ex_Dict_keys:
    print(Ex_Dict.get(i),sep =" ")

print("Extracting all the values of the Dictionary: ",Ex_Dict.values()) #Ex_Dict.values() gives list of all the values
print("Extracting values wrt the keys of the Dictionary: ",Ex_Dict.items()) #Ex_Dict.items() gives list of all the values
print("To check if the key is present in the Dictionary: ","age" in Ex_Dict) #Checking if the key is present in the Dictionary
Ex_Dict.update({"age":11}) #This dictionary.update() updates the value of a key of the dictionary
print("Updating the value of age: ",Ex_Dict)
Ex_Dict["subjects"]=["Phonics,Finance,Politics"]
print("The updated Dictionary is: ",Ex_Dict)
pop_try=Ex_Dict.pop("age")
print("Printing Dictionary after popping age: ",Ex_Dict)
pop_item_try=Ex_Dict.popitem()
print("printing Dictionary after pop_item: ",Ex_Dict)
