from collections import defaultdict
"""
Kruskal's MST Algorithm
Time Complexity: 
Sorting the edges -> O(E*log(E))
Union-Find operations on a disjoint set for E times -> O(E)
In sum, O(E*log(E) + O(E)) ~ O(E*log(E))
"""
class Kruskal:
    def __init__(self):
        self.graph = defaultdict(int)
    
    def getMST(self, edges):
        edges.sort(key=lambda x: x[2])
        print edges
        mst = []
        for u,v,w in edges:
            p1, w1 = self._find(u)
            p2, w2 = self._find(v)

            if p1 == p2:
                continue
        
            if w1 > w2:
                self._union(p1, p2)
            else:
                self._union(p2, p1)
            mst.append((u,v,w))
        return mst
    
    def _find(self, u):
        if self.graph.get(u) <= 0:
            return [u, self.graph.get(u)]
        return self._find(self.graph.get(u))
    
    def _union(self, u,v):
        self.graph[v] = u
        self.graph[u] -= 1

ob = Kruskal()
#edges = [[3,4,4],[3,5,2],[1,3,3],[1,4,5],[2,5,5],[1,2,1]]
edges = [["A","D",1],["D","E",6],["E","F",2],["C","F",4],["C","B",1],["A","B",3],["B","D",3],["C","D",1],["C","E",5]]
print ob.getMST(edges)