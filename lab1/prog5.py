str1 = input("String 1: ")
str2 = input("String 2: ")
str3 = input("String 3: ")

l1 = list(str1)
l2 = list(str2)
l3 = list(str3)

i = 0
while i < len(str1):
	flag = 1
	for j in range(len(str2)):
		if (i + j >= len(l1)) or (l1[i+j] != l2[j]):
			flag = 0
			break
	if flag:
		del l1[i:i+len(str2)]
		l1.insert(i, str3)
		i += len(str3) - 1
	i += 1

str = ""
for i in range(len(l1)):
	str += l1[i]

print("Replaced String:", str)