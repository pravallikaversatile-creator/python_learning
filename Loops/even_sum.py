"""Write a program to input number N and print the sum of even numbers from 1 to N"""

Number=int(input("Enter the Number: "))
Numbers=Number
if (Number%2) != 0:
    Number-=1
add=0
for i in range (2,Number+1,2):
    add+=i

print("Sum of Even numbers from 1 to ",Numbers," is: ",add,",",sep="")


