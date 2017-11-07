from lab7.MinHeap import BinaryMinHeap


class Vertex:
    def __init__(self, i):
        self.index = i
        self.color = "white"
        self.dist = float('inf')
        self.pred = None
        self.adj = []

    def __lt__(self, other):
        return self.dist < other.dist

    def __le__(self, other):
        return self.dist <= other.dist

    def __gt__(self, other):
        return self.dist > other.dist

    def __ge__(self, other):
        return self.dist >= other.dist


class AdjListG:
    def __init__(self, n):
        self.l = [Vertex(x) for x in range(n)]

    def addEdge(self, a, b, weight):
        if b not in self.l[a].adj:
            self.l[a].adj.append([b, weight])

    def dijkstra(self, s):
        for u in self.l:
            u.dist = float('inf')
        s.dist = 0
        l = []
        for u in self.l:
            l.append(u)
        H = BinaryMinHeap(l)
        while H.len:
            w = H.extractMin()
            for v in w.adj:
                d = v[1]
                v = self.l[v[0]]
                if w.dist + d < v.dist:
                    v.dist = w.dist + d
                    v.pred = w
            H.buildHeap()

    def __str__(self):
        print("The Adjacency List is:")
        for i in range(len(self.l)):
            print("Vertex", i, "(" + str(self.l[i].dist) + ")", ":", end=" ")
            for j in self.l[i].adj:
                print(str(j[0]) + "(" + str(j[1]) + ")", end=" ")
            print()
        return ""


n = int(input("Enter the no. of vertices: "))
AL = AdjListG(n)
print("Enter the edges with weights:")
while True:
    s = input()
    if not s:
        break
    a, b, w = map(int, s.split())
    AL.addEdge(a, b, w)

print(AL)
s = int(input("Enter source vertex: "))
print()
AL.dijkstra(AL.l[s])
print(AL)
for i in range(len(AL.l)):
    print("Shortest Path from", i, "to 0:")
    print(AL.l[i].index, end=" ")
    tmp = AL.l[i].pred
    while tmp is not None:
        print("->", tmp.index, end=" ")
        tmp = tmp.pred
    print()
