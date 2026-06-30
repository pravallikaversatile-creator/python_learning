#Reading an already created file
f=open("file1.txt","rt") #Opening the already present txt file to read
# print(f.read()) #Prints the contents of the file on terminal to read
# print(f.readline()) #Reads the first line of the file
# print(f.readlines()) #Reads the file content line by line
for line in f:
    print(line,end=" ") #Reading the contents line by line 
#print(f.read(5)) #Reads the first 5 characters of the file
f.close() #closing the file
f=open("file1.txt","wt") #opening the file, file1.txt in write mode
f.write("I am writing into the File.") #writing into the file
f=open("file1.txt","at") #Opening the file in Append mode
f.write(" Later I will append into it.") #Appending into the file
f.writelines([" This file is interesting.\n" "It has lot of information\n"])
f.close()
with open("file1.txt","r") as f:
    print(f.read()) #Auto closes the file after reading
with open("file1.txt","w") as f:
    f.write("I am attempting autoclosing of file after writing. This is a very intersting file.") #Auto closes the file after writing
f=open("file1.txt","r")
f.seek(5) #Moves file pointer to 5th Byte
print("Printing file contents from 5th Byte.\n")
for line in f:
    print(line,end=" ") #From 5th Byte, Reads the contents line by line 
f.tell() #Tells the current file pointer position
import os
print(os.path.exists("file1.txt"))
#Exception Handling
try:
    with open ("file1.txt","r") as f:
        print(f.read())
except FileNotFoundError:
    print("File Not Found")
with open("file1.txt","r") as f:
    for line in f:
        print(line.strip()) #It strips out trailing characters at the end of each line and prints it


#Copying data from one file to other
with open ("file1.txt","r") as f,open ("file2.txt","w") as f1,open ("file3.txt","w") as f2:
    for line in f:
       f1.write(line.strip() + "\n")
       f2.write(line.strip())

