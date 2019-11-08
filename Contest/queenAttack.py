class Solution(object):
    def _getBoardSize(self, cells):
        m = n = 0
        for i, j in cells:
            m, n = max(i,m), max(j,n)
        return [m,n]
    
    def _createMatrix(self, queens, m, n):
        matrix = [[0 for j in range(n)] for i in range(m)]
        for q in queens:
            matrix[q[0]][q[1]] = 1
        return matrix
    
    def _checkThreat(self, matrix, king):
        dirs = ((0,1), (1,0), (-1,0), (0,-1), (1,1), (-1,-1), (1,-1), (-1,1))
        attackQueens = []
        m, n = len(matrix), len(matrix[0])
        
        for d in dirs:
            cell = self._DFS(matrix, king, d, m, n)
            if cell:
                attackQueens.append(cell)
        return attackQueens
            
    def _DFS(self, matrix, node, direction, m, n):
        x, y = node[0] + direction[0], node[1] + direction[1]
        if 0 <= x < m and 0 <= y < n:
            if matrix[x][y] == 1:
                return [x,y]
            else:
                return self._DFS(matrix, [x,y], direction, m, n)
        
    def queensAttacktheKing(self, queens, king):
        """
        :type queens: List[List[int]]
        :type king: List[int]
        :rtype: List[List[int]]
        """
        m, n = self._getBoardSize(queens + [king])
        m, n = m + 1, n + 1
        
        matrix = self._createMatrix(queens, m, n)
        
        return self._checkThreat(matrix, king)
        
# queens = [[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]]
# king = [0,0]        

# queens = [[0,0],[1,1],[2,2],[3,4],[3,5],[4,4],[4,5]]
# king = [3,3]

queens = [[5,6],[7,7],[2,1],[0,7],[1,6],[5,1],[3,7],[0,3],[4,0],[1,2],[6,3],[5,0],[0,4],[2,2],[1,1],[6,4],[5,4],[0,0],[2,6],[4,5],[5,2],[1,4],[7,5],[2,3],[0,5],[4,2],[1,0],[2,7],[0,1],[4,6],[6,1],[0,6],[4,3],[1,7]]
king = [3,4]

ob = Solution()
print(ob.queensAttacktheKing(queens, king))