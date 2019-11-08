def makeGraph(words):
  graph = {}
  for w in words:
    graph[w] = []
  
  for w in words:
    nextWord = getNext(w)
    for nw in nextWord:
      if nw == w:
        continue
      if nw in graph:
        graph[nw].append(w)
  return graph

def getNext(word):
  nextWords = []
  for i in range(len(word)):
    for j in range(97,123):
      nw = word[:i] + chr(j) + word[i+1:]
      nextWords.append(nw)
  return nextWords

def BFS(graph, source, target):
  pathLen = 0      
  BFSQueue = [[source, 0]]
  visited = set()
  visited.add(source)

  while(BFSQueue != []):
    node = BFSQueue.pop(0)
    node, pathLen = node[0], node[1]
    if node == target:
      return pathLen
    for nei in graph[node]:
      if nei not in visited:
        visited.add(nei)
        BFSQueue.append([nei,pathLen+1])
  return -1
     
def shortestWordEditPath(source, target, words):  
  words += [source]
  graph = makeGraph(words)
  return BFS(graph, source, target)


source = "bit"
target = "dog"
words = ["but", "put", "big", "pot", "pog", "dog", "lot"]

print shortestWordEditPath(source, target, words)