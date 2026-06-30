#Understanding continue

n=0
while n<5:
	if n==2:
		n+=1
		continue

	print(n,sep="\n")
	n+=1

print("I am outside while loop now")
