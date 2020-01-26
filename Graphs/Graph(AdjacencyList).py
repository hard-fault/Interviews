"""
GRAPH

Store: 
    Adjacency list 

Search: 
    1) BFS 
    2) DFS

Find:
    1) If a path exists bwteen two nodes and print the path
    2) Cycle, if any

Adavanced:
    1) Shortest path using Dijkstra's algorithm
    2) Shortest path using Bellman Ford algorithm
    3) Topological sorting
    4) Minimum spanning tree
    5) Independent set
    6) Vertex cover
"""

from collections import defaultdict

class node:
    def __init__(self, value):
        self.value = value
        self.children = []
    
class Graph:
    def __init__(self):
        self.adjacencyList = defaultdict(list)
        self.visited = {}
        self.BFSQueue = []
    
    def addEdge(self,u,v):
        self.adjacencyList[u].append(v)
        self.visited[u] = False
        self.visited[v] = False
        
    def printList(self):
        nodes = self.adjacencyList.keys()
        for n in nodes:
            print "{} ->{}".format(n,self.adjacencyList[n])
    
    def DFS(self,u):
        self.visited[u] = True
        print u,
        for node in self.adjacencyList[u]:
            if self.visited[node] != True:
                self.DFS(node)
    
    def BFS(self,u):
        self.visited[u] = True
        print u,
        
        for node in self.adjacencyList[u]:
            if node not in self.BFSQueue and self.visited[node] == False:
                self.BFSQueue.append(node)
        print self.BFSQueue

        if len(self.BFSQueue) > 0:
            self.BFS(self.BFSQueue.pop(0))

obj = Graph()
"""
1--->2--->5
| \ |    ^
|  \|    |
v   v    |
3   4--->6
***DFS***
1 2 5 4 6 3
***BFS***

"""

obj.addEdge(1,2)
obj.addEdge(1,3)
obj.addEdge(1,4)
obj.addEdge(2,5)
obj.addEdge(2,4)
obj.addEdge(4,6)
obj.addEdge(6,5)
obj.printList()


#print "***DFS***"
#obj.DFS(1)

#print "***BFS***"
#obj.BFS(1)



