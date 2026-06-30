""" List Example """
Ex_List=[1,3.5,4+8j,"Pravz"]
print("printing whole list: ",Ex_List)
print("Printing List type: ",type(Ex_List))
print("Accessing an indexed location in List: ",Ex_List[3]) # It allows negetive indexing aswell [-1 to -len] for -ve and [0 to len-1] for +ve indexing
print("Accessing a Sliced portion of the List: ",Ex_List[1:3]) #Slicing preserves properties
print("Accessing a Sliced portion of the List: ",Ex_List[:3]) #Slicing preserves properties
print("Accessing a Sliced portion of the List: ",Ex_List[2:]) #Slicing preserves properties
print("Checking if a variable 'Pravz' is in the List: ",'Pravz' in Ex_List)
print("Checking if a variable '3+9j' is in the List: ",'3+9j' in Ex_List)
Ex_List[2]="True"
print("Updated Ex_List[2] with 'True': ",Ex_List)
print("Original List is: ",Ex_List)
Ex_List[1:3]=[1,2+9j,[2,9,7+9j]] #List allows Duplicating
print("Updated List is: ",Ex_List)
Ex_List.insert(1,'True') #Inserting can happen at any index location in the List
print("Updated List after inserting 'True' at index 1: ",Ex_List)
Ex_List.append("The last Variable")
print("Updated List after appending: ",Ex_List) #Appending happens at the end
Ex_List_2=['abcd', 3.65, 9+10j,34]
Ex_List.extend(Ex_List_2)
print("The extended List is: ",Ex_List) #This prints out the extended List
Ex_List_extended=Ex_List.extend(Ex_List_2)
print("The extended List when function is returned is: ",Ex_List_extended) #This prints out "None" as extend function returns None
print("Length of the List is: ",len(Ex_List))
print(Ex_List)

""" Tuple Example """
Ex_Tuple=(1,3.5,4+8j,"Pravz")
print("printing whole Tuple: ",Ex_Tuple)
print("Printing Tuple type: ",type(Ex_Tuple))
print("Accessing an indexed location in Tuple: ",Ex_Tuple[2])
print("Accessing a Sliced portion of the Tuple: ",Ex_Tuple[1:3]) #Slicing preserves properties
#Ex_Tuple[2]="True" #TypeError: 'tuple' object does not support item assignment
print("Cannot Update Tuple. It is not Mutable")
print("Tuple Variables are: ")
for i in Ex_Tuple:
    print(i,sep=" ")
