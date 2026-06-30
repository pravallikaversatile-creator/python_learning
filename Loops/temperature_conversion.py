import math
Start,End,Step=map(int,input("Enter Start, End and Step sizes for the Farenheit range to be converted to Celsius. Enter these values in a single line seperated by space: ").split())

if 0 <= Start <= 80 and Start <= End <=  900 and 0 <= Step <= 40:
    for i in range(Start,End+1,Step):
        Celsius=(i-32)*(5/9)
        if(Celsius>=0):
            print("Celsius value for Farenheit ",i," is: ",math.floor(Celsius),".",sep="",end="\n")
        else:
            print("Celsius value for Farenheit",i," is: ",math.ceil(Celsius),".",sep="",end="\n")
else:
    print("Invalid range of inputs provided")


