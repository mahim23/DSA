from lab2.LinkedList import *

hashTable = [None for i in range(30)]


def hashCode(key):
    x = 1
    hash = 0
    for i in range(len(key)):
        hash += ord(key[i]) * x
        x *= 33
    return hash


def hashMap(hash):
    index = hash % 30
    return index


def insert(key, val=None):
    index = hashMap(hashCode(key))
    if not hashTable[index]:
        l = LinkedList()
        l.insertAtIndex((key, val), 0)
        hashTable[index] = l
    else:
        l = hashTable[index]
        l.insertAtIndex((key, val), 0)


def search(key):
    index = hashMap(hashCode(key))
    if hashTable[index]:
        l = hashTable[index]
        node = l.search((key, None))
        if node:
            return True
    else:
        return False


def keys():
    k = []
    for i in hashTable:
        if i:
            tmp = i.head
            while tmp.next:
                k.append(tmp.next.val[0])
                tmp = tmp.next
    return k


file = open("ispell.dict", "r")
words = file.readlines()


for word in words:
    insert(word[:-1])


letters = [chr(x) for x in range(97, 123)]
print("\n\tAuto Correct\n")
while True:
    word = input("Enter word to be checked (0 to exit): ")
    if word == "0":
        print("Exiting...")
        break
    if search(word):
        print("Correct Spelling\n")
    else:
        alt = []
        word = list(word)
        t = word[:]
        for i in range(len(word)):
            for j in range(26):
                t = list(t)
                t[i] = letters[j]
                t = ''.join(t)
                if search(t):
                    alt.append(t)
            t = word[:]
        print("Incorrect Spelling\nSuggestions:", alt, "\n")

