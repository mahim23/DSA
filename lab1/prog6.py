from time import process_time
from random import randint
import matplotlib.pyplot as plt

def bubbleSort(l, n):
	bubble_start = process_time()
	for i in range(n-1, 0, -1):
		for j in range(i):
			if l[j] > l[j+1]:
				l[j+1], l[j] = l[j], l[j+1]
	bubble = process_time() - bubble_start
	return bubble

def selSort(l, n):
	sel_start = process_time()
	for i in range(n-1):
		min = i
		for j in range(i, n):
			if l2[j] < l2[min]:
				min = j
		l2[min], l2[i] = l2[i], l2[min]
	sel = process_time() - sel_start
	return sel


xAxis = range(100, 10000, 100)
yB = []
yS = []
for i in xAxis:
	l = [randint(1, 1000) for x in range(i)]
	l2 = l[:]
	yB.append(bubbleSort(l, i))
	yS.append(selSort(l2, i))

plt.plot(xAxis, yB, 'b-', xAxis, yS, 'r-')
plt.show()
