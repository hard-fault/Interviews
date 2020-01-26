import collections
import heapq

class Dijkstras:
    def _makeGraph(self, edges):
        graph = collections.defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v,w))
            graph[v].append((u,w))
        return graph

    def getShortestPath(self, edges, src):
        graph = self._makeGraph(edges)

        minHeap, visited = [(0,src)], set()
        shortestDist = {}

        while minHeap:
            cost, node = heapq.heappop(minHeap)

            if node in shortestDist:
                continue
            
            shortestDist[node] = cost
            neighbors = graph[node]
            for nei,c in neighbors:
                prevCost = shortestDist.get(nei, None)
                currCost = cost + c
                if prevCost is None or currCost < prevCost:
                    heapq.heappush(minHeap, (currCost, nei))
        
        return shortestDist

if __name__ == "__main__":
    edges = [
        ("A", "B", 5),
        ("A", "D", 9),
        ("B", "C", 2),
        ("A", "E", 2),
        ("D", "F", 2),
        ("E", "F", 3),
        ("C", "D", 3)
    ]

    # edges = [
    #     ("A", "B", 7),
    #     ("A", "D", 5),
    #     ("B", "C", 8),
    #     ("B", "D", 9),
    #     ("B", "E", 7),
    #     ("C", "E", 5),
    #     ("D", "E", 15),
    #     ("D", "F", 6),
    #     ("E", "F", 8),
    #     ("E", "G", 9),
    #     ("F", "G", 11)
    # ]
    print "=== Dijkstra ==="
    print edges
    ob = Dijkstras()
    print ob.getShortestPath(edges,"C")