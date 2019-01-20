
def rotateMat(mat):
    n = len(mat)
    for i in range(0,int(n/2)):
        for j in range(i,n-1-i):
            temp = mat[i][j]
            mat[i][j] = mat[j][n-1-i]
            mat[j][n-1-i] = mat[n-1-i][n-1-j]
            mat[n-1-i][n-1-j] = mat[n-1-j][i]
            mat[n-1-j][i] = temp
    return mat

mat = [
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20],
    [21,22,23,24,25]
]

print rotateMat(mat)