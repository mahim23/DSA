def factRec(n):
	if n == 1:
		return 1
	return n*factRec(n-1)


def factIte(n):
	fact = 1
	for i in range(2,n+1):
		fact *= i
	return fact


x = int(input("Enter no.: "))

print("\nFactorial calculated recursively =", factRec(x))
print("Factorial calculated iteratively =", factIte(x), "\n")