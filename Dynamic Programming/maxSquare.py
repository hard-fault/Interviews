"""
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.


Input:

1 0 1 0 0
1 0 0 1 1
1 0 1 1 1
1 0 1 1 1

Output: 4


Summary:

We need to find the largest square comprising of all ones in the given m x n matrix. In other words we need to find the largest set of connected ones in the given matrix that forms a square.
"""

input = [[1,0,1,0,0],[1,0,1,1,1],[1,1,1,1,1],[1,0,1,1,1]]

def getMaxSquare(input):
    dpTable = [[]] * len(input)
    dpTable[0] = input[0]

    for i in range(1,len(input)):
        dpTable[i] = [0]*len(input[i])
        dpTable[i][0] = input[i][0]

    maxSquare = -1
    for i in range(1,len(dpTable)):
        for j in range(1,len(dpTable[i])):
            if input[i][j] == 1:
                dpTable[i][j]=input[i][j]+min(dpTable[i][j-1],dpTable[i-1][j],dpTable[i-1][j-1])
            if dpTable[i][j] > maxSquare:
                maxSquare = dpTable[i][j]
    print dpTable
    return maxSquare * maxSquare

print getMaxSquare(input)
