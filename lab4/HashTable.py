from lab2.LinkedList import *

hashTable = [None for i in range(30)]


def hashCode(key):
    x = 33
    hash = 0
    for i in range(len(key)):
        hash += ord(key[i])
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


inputs = ["abc", "cat", "act", "hello", "cat", "act", "cat", "act"]

for i in inputs:
    insert(i)

print(search("xyz"))
print(search("lmn"))

print(keys())
