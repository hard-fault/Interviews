from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.DFS_List = []
        self.BFS_List = []
        self.BFS_queue = []

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def printGraph(self):
        print self.graph

    def DFS(self, v, visted):
        visited[v] = 1

        self.DFS_List.append(v)

        for u in self.graph[v]:
            if visited[u] == 0:
                self.DFS(u,visited)

    def BFS(self, v, visited):
        visited[v] = 1

        for u in self.graph[v]:
            if visited[u] == 0:
                self.BFS_queue.append(u)
                self.BFS_List.append(u)

        if len(self.BFS_queue) > 0:
            v = self.BFS_queue.pop(0)
            self.BFS(v,visited)

graph_matrix = [
[0,1,0,1,0],
[0,0,1,0,1],
[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,0]
]

g = Graph()

for i in range(len(graph_matrix)):
    for j in range(len(graph_matrix[i])):
        if graph_matrix[i][j] == 1:
            g.addEdge(i,j)

visited = [0] * len(graph_matrix)

g.DFS(0,visited)

visited = [0] * len(graph_matrix)
g.BFS(0,visited)

print "DFS"
print g.DFS_List

print "BFS"
print g.BFS_List



