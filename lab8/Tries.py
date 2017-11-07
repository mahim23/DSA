class TriesDS:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False


class Tries:
    def __init__(self):
        self.node = TriesDS()

    def insert(self, k):
        p = k
        temp = self.node
        t = 0
        for i in range(len(p)):
            m = ord(p[t]) - ord('a')
            if temp.children[m] is None:
                temp.children[m] = TriesDS()
                temp = temp.children[m]
                t = t + 1
            else:
                temp = temp.children[m]
                t = t + 1
        temp.isEnd = True

    def search(self, key):
        temp = self.node
        for i in range(len(key)):
            m = ord(key[i]) - ord('a')
            if temp.children[m] is not None:
                temp = temp.children[m]
            else:
                return False
        if temp.isEnd:
            return True
        else:
            return False


def main():
    l = Tries()
    # l.insert("ar")
    p = ["a", "arr", "who", "whose"]
    for w in p:
        l.insert(w)
    print(l.search("array"))


if __name__ == '__main__':
    main()
