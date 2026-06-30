num1,num2=map(int,input("Enter two numbers seperated by space: ").split())
print("numbers before swaping are num1=",num1," num2=",num2,".",sep="")
num1=num1+num2
num2=num1-num2
num1=num1-num2
print("numbers after swaping are num1=",num1," num2=",num2,".",sep="")
