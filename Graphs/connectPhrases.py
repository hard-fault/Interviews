class Connect:
    def __init__(self):
        self.result = []

    def _makeGraph(self, phrases):
        graph, startNodes = {}, []
        for p in phrases:
            last = p.split(" ")[-1]
            graph[last] = []

        for p in phrases:
            first = p.split(" ")[0]
            if first in graph:
                graph[first].append(p)
            else:
                startNodes.append(p)
        return [graph, startNodes]

    def _DFS(self, graph, node, visited, combined):
        nodeSplit = node.split(" ")
        neighbors = graph[nodeSplit[-1]]
        
        if not neighbors:
            self.result.append(combined)

        for nei in neighbors:
            if nei not in visited:
                visited.add(nei)
                self._DFS(graph, nei, visited, combined +" "+" ".join(nei.split(" ")[1:]))

    def connectPhrases(self, phrases):
        phraseGraph, startPhrases = self._makeGraph(phrases)
        print (phraseGraph, startPhrases)
        result = []
        for start in startPhrases:
            visited = {start}
            self._DFS(phraseGraph, start, visited, start)
        return self.result

phrases = ["a b c", "c d e", "c m u", "e f g", "m n o", "p q r","r s t"]
expected = ["a b c d e f g", "a b c m u", "m n o", "p q r s t"]

ob = Connect()
print(ob.connectPhrases(phrases))