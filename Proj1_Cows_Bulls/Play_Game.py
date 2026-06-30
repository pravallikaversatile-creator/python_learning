import random

Name=input("Please Enter your name to play the game: ")
print(f"Hi {Name}, You have 8 chances to guess the correct number, Let's start: ")

while True:
    Random_value = random.randint(100, 999)
    digits = list(str(Random_value))
    if len(set(digits)) == 3:   # all digits unique
        break

Generated_Value =Random_value
digits = []
while Random_value > 0:
    digits.append(Random_value % 10)
    Random_value //= 10
digits.reverse()
chances=0
pos_val_dict = {i+1: digits[i] for i in range(len(digits))}
#print(pos_val_dict)
#pos_val_dict = {pos: val for pos, val in enumerate(digits, start=1)}
bulls=0
for chances in range(8):
    if bulls == 3 :
        break
    else:
        Guess_Number= int(input(f"Hey {Name}! This is your chance {chances+1} Please guess your number: "))
        Guess_digits=[]
        while Guess_Number > 0:
            Guess_digits.append(Guess_Number % 10)
            Guess_Number //= 10
        Guess_digits.reverse()
        Guess_pos_val_dict = {i+1: Guess_digits[i] for i in range(len(Guess_digits))}

        # Bulls: key AND value match
        bulls = sum(1 for k in pos_val_dict if pos_val_dict[k] == Guess_pos_val_dict[k])

        # Cows: value matches irrespective of key, but not counted as bulls
        pos_values = list(pos_val_dict.values())
        guess_values = list(Guess_pos_val_dict.values())

        cows = 0
        for val in guess_values:
            if val in pos_values:
                cows += 1
                pos_values.remove(val)   # prevent double counting
        print(f"Your bulls value for the attempt is: {bulls} and cows value for the attempt is: {cows}")
        #chances+=1

if bulls==3:
    print("Congrats! Well Done")
    print(f"The random number is: {Generated_Value}")
else:
    print("Better Luck Next Time")
    print(f"The random number is: {Generated_Value}")

