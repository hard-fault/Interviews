"""
1) Find the increasing sum path in the matrix
"""
DFS_List = []

def dfs(matrix, row, col):
    if (row < 0 or row >=len(matrix)) or (col < 0 or col >=len(matrix)):
        return 0

    for i in range(row,len(matrix)):
        for j in range(col, len(matrix[i])):
            if matrix[i][j] == 1:
                DFS_List.append([i,j])
                dfs(matrix, i+1, j)
                dfs(matrix, i+1, j+1)
                #dfs(matrix, i-1, j-1)
                matrix[i][j] = 0
            else:
                return


adjacencyMatrix = [
[1,1,0,0,0,0,0],
[1,1,1,0,1,1,1],
[1,1,0,0,0,0,0],
[0,0,1,0,1,0,0],
[0,1,0,1,0,0,0],
[0,1,0,0,0,0,0]
]

matrix = [
[9,9,4],
[6,6,8],
[2,1,1]
]

for i in range(len(adjacencyMatrix)):
    for j in range(len(adjacencyMatrix[i])):
        if adjacencyMatrix[i][j] == 1:
            DFS_List = []
            dfs(adjacencyMatrix, i, j)
            print DFS_List

