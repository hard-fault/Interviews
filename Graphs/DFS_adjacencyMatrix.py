DFS_List = []

def dfs(matrix, i, visited):
    if i < 0 or i >=len(matrix):
        return 0
    visited[i] = 1
    for j in range(len(matrix[i])):
        if matrix[i][j] == 1 and visited[j] == 0:
            matrix[i][j] = 0
            DFS_List.append(j)
            dfs(matrix, j, visited)


adjacencyMatrix = [
[1,1,0,0,0,0],
[1,1,1,0,0,1],
[0,1,0,0,0,0],
[0,0,0,0,1,0],
[0,1,0,1,0,0],
[0,1,0,0,0,0]
]


visited = [0] * len(adjacencyMatrix)
DFS_List.append(0)

dfs(adjacencyMatrix, 0, visited)

print DFS_List
