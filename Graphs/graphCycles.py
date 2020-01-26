from collections import defaultdict
class Graph:
    def _makeGraph(self, edges):
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        return graph
    
    def getCycleNodes(self, edges):
        graph = self._makeGraph(edges)
        self.cycleFound, self.cycleNodes = False, []

        
        self.visited, self.recStack = set(), []
        self._DFS(1, -1, graph)
        
        if self.cycleFound:
            print("Cycle path:", self.cycleNodes)
        else:
            print("No cycle")
    
    def _DFS(self, node, prev, graph):
        self.visited.add(node)
        self.recStack.append(node)

        for nei in graph[node]:
            if nei == prev:
                continue
            if nei not in self.visited:
                self._DFS(nei, node, graph)
            elif nei in self.visited and not self.cycleFound:
                self.cycleFound = True
                self.cycleNodes = self.recStack[:]

        self.recStack.pop()

graph = Graph()
edges = [[1,2], [2,3], [2,4], [5,4], [3,2], [5,3], [3,6]]
#edges = [[6,5], [5,3], [3,2], [2,1], [1,3], [3,4]]
#edges = [[1,2], [2,3], [3,4], [3,5], [4,7], [4,6], [5,6],[5,9],[7,8], [6,10], [10,11], [11,12], [12,13], [11,13]]


graph.getCycleNodes(edges)




