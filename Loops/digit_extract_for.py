Number=input("Enter the 6 digit number: ")
Even=0
Odd=0
for i in Number:
    if int(i)%2 == 0:
        Even+=int(i)
    else:
        Odd+=int(i)

print("Sum of Even digits in the number is: ",Even," and sum of odd digits is: ",Odd,".",sep="")
