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
        # if a not in self.l[b].adj:
        #     self.l[b].adj.append(a)

    def BFS(self, s):
        self.l[s].dist = 0
        self.l[s].color = "gray"
        Q = [self.l[s]]
        p = []
        while len(Q):
            u = Q.pop(0)
            p.append(self.l.index(u))
            for v in u.adj:
                v = self.l[v]
                if v.color == "white":
                    v.dist = u.dist + 1
                    v.color = "gray"
                    v.pred = u
                    Q.append(v)
                elif v.color == "black" and u.pred is not v:
                    return "cycle"
            u.color = "black"
        return p

    def cycle(self):
        l = list(range(len(self.l)))
        while len(l):
            p = self.BFS(l[0])
            if p == "cycle":
                return True
            for i in p:
                l.remove(i)
        return False


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
print("Cycle present: ", AL.cycle())
