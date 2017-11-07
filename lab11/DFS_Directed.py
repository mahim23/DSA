class Vertex:
    def __init__(self):
        self.color = "white"
        self.dist = float('inf')
        self.pred = None
        self.adj = []
        self.startTime = 0
        self.endTime = 0


class AdjListG:

    def __init__(self, n):
        self.l = [Vertex() for _ in range(n)]
        self.time = 1
        self.treeEdges = []
        self.backEdges = []
        self.forwardEdges = []
        self.crossEdges = []

    def addEdge(self, a, b):
        if b not in self.l[a].adj:
            self.l[a].adj.append(b)

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

    def DFS(self, u):
        u.color = "gray"
        u.startTime = self.time
        self.time += 1
        i = self.l.index(u)
        print("Vertex: ", i)
        for v in u.adj:
            j = v
            v = self.l[v]
            if v.color == "white":
                self.DFS(v)
                v.pred = u
                self.treeEdges.append(str(i) + "->" + str(j))
            else:
                if v.startTime > u.startTime:
                    self.forwardEdges.append(str(i) + "->" + str(j))
                elif v.endTime == 0:
                    self.backEdges.append(str(i) + "->" + str(j))
                else:
                    self.crossEdges.append(str(i) + "->" + str(j))
        u.color = "black"
        u.endTime = self.time
        self.time += 1


    def __str__(self):
        print("The Adjacency List is:")
        for i in range(len(self.l)):
            print("Vertex", i, "time [", self.l[i].startTime, ",", self.l[i].endTime, "]", ":", end=" ")
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
s = int(input("Enter source vertex: "))
print()
AL.DFS(AL.l[s])
print()
print(AL)
print("Tree Edges:", AL.treeEdges)
print("Back Edges:", AL.backEdges)
print("Forward Edges:", AL.forwardEdges)
print("Cross Edges:", AL.crossEdges)


# 0 1
# 0 2
# 1 4
# 4 5
# 4 6
# 4 7
# 2 3
# 3 7
# 5 1
# 5 0
# 5 6
# 7 6
