def fiboIte(n):
	a = 0
	b = 1
	print(a, end=" ")
	for i in range(1,n):
		print(b, end=" ")
		a, b = b, a+b
	print()

def fiboRec(n):
	if n == 2:
		return 1
	elif n == 1:
		return 0
	return fiboRec(n-1) + fiboRec(n-2)

x = int(input("Enter n: "))

print("\nFibonacci Series (iteration):", end=" ")
fiboIte(x)

print("\nFibonacci Series (recursion):", end=" ")
for i in range(1, x+1):
	print(fiboRec(i), end=" ")