from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.BFSQueue = []

    def _makeGraph(self, edges):
        for src, dest in edges:
            self.graph[src].append(dest)
            self.graph[dest].append(src)

    def driverFunction(self, nodes, edges):
        self._makeGraph(edges)

        #Get start nodes if necessary.
        startNodes = nodes

        #Traverse the graph
        self._traverseGraph(startNodes)
    
    def _DFS(self, node, visited):
        print(node)
        neighbors = self.graph[node]

        for nei in neighbors:
            if nei not in visited:
                visited.add(nei)
                self._DFS(nei, visited)
    
    def _BFS(self, node, visited):
        print(node)
        neighbors = self.graph[node]
        
        for nei in neighbors:
            if nei not in visited:
                visited.add(nei)
                self.BFSQueue.append(nei)
        
        if self.BFSQueue:
            self._BFS(self.BFSQueue.pop(0), visited)
    
    def _traverseGraph(self, nodes):
        print("\nDFS:")
        for n in nodes:
            visited = {n}
            self._DFS(n, visited)

        print("\nBFS:")
        for n in nodes:
            visited = {n}
            self._BFS(n, visited)
            
    def _shortestPath(self, source, dest):
        pathLength = 0
        return pathLength
    
    def _detectCycles(self):
        cycles = []
        return cycles
    

graph = Graph()
edges = [(1 , 2), (1 , 3), (2 , 4), (2, 6), (4 , 5), (4 , 7)]
nodes = [1]

graph.driverFunction(nodes, edges)