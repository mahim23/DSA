class AdjListG:

    def __init__(self, n):
        self.l = [[] for _ in range(n)]

    def addEdge(self, a, b):
        if b not in self.l[a]:
            self.l[a].append(b)
        if a not in self.l[b]:
            self.l[b].append(a)

    def __str__(self):
        print("The Adjacency List is:")
        for i in range(len(self.l)):
            print("Vertex", i, ":", end=" ")
            for j in self.l[i]:
                print(j, end=" ")
            print()
        return ""


class AdjMatG:

    def __init__(self, n):
        self.m = [[0 for _ in range(n)] for _ in range(n)]

    def addEdge(self, a, b):
        self.m[a][b] = 1
        self.m[b][a] = 1

    def __str__(self):
        print("The Adjacency Matrix is:")
        for i in self.m:
            for j in i:
                print(j, end=" ")
            print()
        return ""


def main():
    n = int(input("Enter the no. of vertices: "))
    AM = AdjMatG(n)
    AL = AdjListG(n)
    print("Enter the edges:")
    while True:
        s = input()
        if not s:
            break
        a, b = map(int, s.split())
        AM.addEdge(a, b)
        AL.addEdge(a, b)

    print(AM)
    print(AL)


if __name__ == '__main__':
    main()
