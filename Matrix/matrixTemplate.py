class Matrix:
    def printDiagonal(self, mat):
        n = len(mat)
        for col in range(n):
            j = col
            for i in range(n-col):
                print(mat[i][j])
                j += 1

mat = [[10,20,30,40,50], [60,70,80,90,100], [110,120,130,140,150], [160,170,180,190,200],[210,220,230,240,250]]
matrix = Matrix()
matrix.printDiagonal(mat)