Number=int(input("Enter the 6 digit number: "))
Even=0
Odd=0
while Number > 0:
    digit=Number%10
    if digit % 2 == 0:
        Even+=digit
    else:
        Odd+=digit
    Number//=10 

print("Sum of Even digits in the number is: ",Even," and sum of odd digits is: ",Odd,".",sep="")
