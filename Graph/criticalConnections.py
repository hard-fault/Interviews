from collections import defaultdict

class Solution():
    def makeGraph(self, n, edges):
        graph = defaultdict(list)
        for src, dest in edges:
            graph[src].append(dest)
            graph[dest].append(src)
        return graph
    
    def getDiff(self, li1, li2): 
        li_dif = [i for i in li1 + li2 if i not in li1 or i not in li2] 
        return li_dif 

        return 
    def criticalConnections(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """
        if n == 0:
            return []
        graph = self.makeGraph(n, connections)
        BFSQueue = [0]
        notCritical = set()
        critical = {0:[]}
        
        while BFSQueue:
            node = BFSQueue.pop(0)
            c = critical[node]
            print(node, c)
            for nei in graph[node]:
                print("\t nei -> {}".format(nei))
                if nei not in critical:
                    print("\t nei not visited")
                    BFSQueue.append(nei)
                    critical[nei] = [{node, nei}]
                    print("\t critical[{}]->{}".format(nei, critical[nei]))
                else:
                    print("\t nei already visited")
                    notCommon = self.getDiff(critical[nei], c+[{node, nei}])
                    print("\t notCommon-{}".format(notCommon))
                    # if len(notCommon) > 1:
                        # notCritical = notCritical notCommon
        
        # print (notCritical)

ob = Solution()
n = 4
connections = [[0,1],[1,2],[2,0],[1,3]]
ob.criticalConnections(n, connections)

            
        