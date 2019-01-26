class Solution:
    def __init__(self): 
        self.BFSQueue = []
        
    def BFS(self, grid,i,j,m,n):
        if i >= m or j >= n or i< 0 or j < 0:
            return
        
        grid[i][j] = "0"
        
        if i < m-1 and grid[i+1][j] == "1" and (i+1,j) not in self.BFSQueue:
            self.BFSQueue.append((i+1,j))
        if i > 0 and grid[i-1][j] == "1" and (i-1,j) not in self.BFSQueue:
            self.BFSQueue.append((i-1,j))
        if j < n-1 and grid[i][j+1] == "1" and (i,j+1) not in self.BFSQueue:
            self.BFSQueue.append((i,j+1))
        if j > 0 and grid[i][j-1] == "1" and (i,j-1) not in self.BFSQueue:
            self.BFSQueue.append((i,j-1))
                    
        if len(self.BFSQueue) > 0:
            nextNode = self.BFSQueue.pop(0)
            self.BFS(grid,nextNode[0],nextNode[1],m,n)

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if grid == []:
            return 0
        m = len(grid)
        n = len(grid[0]) 
        
        islands = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    islands += 1
                    self.BFS(grid, i, j, m, n)
                    
        return islands

