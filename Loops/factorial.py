"""Write a program to find the factorial of a number.

Factorial of n is:

n! = n * (n-1) * (n-2) * (n-3)....* 1

Output the factorial of 'n'. If it does not exist, output 'Error'. """

number=int(input("Enter number"))
factorial=1
if(number == 0):
    print("Factioral of ",number,": is: ",factorial,".",sep="")
elif (number < 0):
    print("Factioral of ",number,": is Error")
else:
    for i in range(1,number+1):
        factorial*=i

if(number>0):
    print(factorial)
    #print("Factioral of ",number,": is: ",factorial,".",sep="")

    
