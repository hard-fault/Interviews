from collections import defaultdict
class Graph:
    def countNodes(self, src, edges):
        graph = self._makeGraph(edges)
        self.visited = set()

        return self._DFS(src, 0, graph)

    def _makeGraph(self, edges):
        graph = defaultdict(list)
        for src, dest in edges:
            graph[src].append(dest)
            graph[dest].append(src)
        return graph

    def _DFS(self, node, count, graph):
        self.visited.add(node)
        maxCount = count + 1
        neighbors = graph[node]

        for nei in neighbors:
            if nei not in self.visited:
                childCount = self._DFS(nei, maxCount, graph)
                maxCount = max(maxCount, childCount)
        
        return maxCount

edges = [['A','B'], ['B','C'], ['A','D'], ['A','E'], ['A','C']]#, ['X','Y'], ['X','G'], ['G','D'],['M','A'],['P','M']]
ob = Graph()
print(ob.countNodes('A', edges))    