n = int(input("Enter n: "))

l = []
print("Enter the Array:")

for i in range(n):
	l.append(int(input()))

l2 = l[:]

for i in range(n-1, 0, -1):
	for j in range(i):
		if l[j] > l[i]:
			l[i], l[j] = l[j], l[i]

print("Sorted Array (Bubble Sort): ", l)

for i in range(n-1):
	min = i
	for j in range(i, n):
		if l2[j] < l2[min]:
			min = j
	l2[min], l2[i] = l2[i], l2[min]

print("Sorted Array (Selection Sort): ", l2)