def minFallPath(matrix,i,j):
    m = len(matrix)
    n = len(matrix[0])
    if i<0 or j<0 or i>=m or j>=n:
            return 0

    print("visiting [{},{}] {} ".format(i,j,matrix[i][j]))
    if i+1<m and j-1>=0:
        left = minFallPath(matrix,i+1,j-1)
    else:
        left = 0
    if i+1<m and j>=0 and j<n:
        down = minFallPath(matrix,i+1,j)
    else:
        down = 0
    if i+1<m and j+1<n:
        right = minFallPath(matrix,i+1,j+1)
    else:
        right = 0
    print ("[{}{}] {} returning {}".format(i,j,matrix[i][j],min(left,down,right)+ matrix[i][j]))
    return min(left,down,right)+ matrix[i][j]
    #return left + matrix[i][j]

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print
print (minFallPath(matrix,0,0))



# if i == m-1 and j>=0 and j<n:
#     return matrix[m-1][j]
# elif i < m and j == 0:
#     return matrix[i][0]
# elif i < m and j == n-1:
#     return matrix[i][n-1]