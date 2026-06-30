#Exercise 1 Fibonacci Series

def fib(key):
#    for i in range(0,key):
        if key<=1:
            return key
        return fib(key-1)+fib(key-2)


key=int(input("Enter the key value to derive the fibonacci series from 0 to Key value: "))
print("The fibonacci series is: ")
for i in range (key):
    print(fib(i),end=" ")

print("\n")



#Exercise 2 Power and Exponent

def expo(base,exponent):
    if exponent == 0:
        return 1
    else:
        return base*expo(base,exponent-1)

base,exponent=map(int,input("Enter base and Exponent to be calculated in single line seperated by space: ").split())
print("base raised to the exponent value is: ",expo(base,exponent))

