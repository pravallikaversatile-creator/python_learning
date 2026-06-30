"""Write a program to find x to the power n (i.e., x^n). Take x and n from the user. You need to print the answer.
Note: For this question, you can assume that 0 raised to the power of 0 is 1"""

Base,Exponent = map(int,input("Enter the base and exponent: ").split())
if Base==0 and Exponent==0:
    print("Answer is Error")
else:
    if Exponent == 0:
        print("Answer is: ", 1)
    else:
        Answer=1
        while Exponent > 0 :
            Answer*=Base
            Exponent-=1
        print("Answer is: ",Answer)
