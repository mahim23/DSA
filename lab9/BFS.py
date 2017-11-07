class Vertex:
    def __init__(self):
        self.color = "white"
        self.dist = float('inf')
        self.pred = None
        self.adj = []


class AdjListG:

    def __init__(self, n):
        self.l = [Vertex() for _ in range(n)]

    def addEdge(self, a, b):
        if b not in self.l[a].adj:
            self.l[a].adj.append(b)
        if a not in self.l[b].adj:
            self.l[b].adj.append(a)

    def BFS(self, s):
        self.l[s].dist = 0
        self.l[s].color = "gray"
        Q = [self.l[s]]
        while len(Q):
            u = Q.pop(0)
            for v in u.adj:
                v = self.l[v]
                if v.color == "white":
                    v.dist = u.dist + 1
                    v.color = "gray"
                    v.pred = u
                    Q.append(v)
                    print("Vertex: ", self.l.index(v), "Dist: ", v.dist)
            u.color = "black"

    def __str__(self):
        print("The Adjacency List is:")
        for i in range(len(self.l)):
            print("Vertex", i, ":", end=" ")
            for j in self.l[i].adj:
                print(j, end=" ")
            print()
        return ""


n = int(input("Enter the no. of vertices: "))
AL = AdjListG(n)
print("Enter the edges:")
while True:
    s = input()
    if not s:
        break
    a, b = map(int, s.split())
    AL.addEdge(a, b)

print(AL)

AL.BFS(0)
