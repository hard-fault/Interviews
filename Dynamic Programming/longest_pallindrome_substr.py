import sys
def func(a, i, j):
    if i == j:
        mem[i][j] = True
        return True
    if mem[i][j] == None:
        mem[i][j] = func(a, i+1, j-1)
        if a[i] == a[j]:
            return True
        else:
            return False

a = sys.argv[1]
n = len(a)
mem = [[None]*n for x in xrange(n)]
func(a,0,n-1)

for r in mem:
    print r
