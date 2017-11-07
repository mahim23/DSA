n = int(input("Enter a number: "))

x = int(n**0.5)
for i in range(2, x+1):
	if not n % i:
		print("Not Prime")
		break
else:
	
	print("Prime")
