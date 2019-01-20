
def conquer(a,l,m,r):
    n1 = m - l + 1
    n2 = r - m

    L = [0]*n1
    R = [0]*n2

    for i in range(0,n1):
       L[i] = a[l + i]
    for i in range(0,n2):
        R[i] = a[m + 1 + i]

    i = 0
    j = 0
    k = l

    while(i < n1 and j < n2):
        LL = L[i]
        RR = R[j]
        aa = []
        n11 = len(LL)
        n22 = len(RR)
        ii = 0
        jj = 0
        while (ii < n11 and jj < n22):
            if LL[ii] <= RR[jj]:
                aa.append(LL[ii])
                ii += 1
            else:
                aa.append(RR[jj])
                jj += 1
        a[l] = aa
        i += 1
        j += 1
        l += 1






def divide(a,l,r):
    if l < r:
        m = (l + r) / 2

        divide(a,l,m)
        divide(a,m+1,r)

        conquer(a,l,m,r)




a = [[1,2],[1,9],[5,8],[10,32,40],[1,9],[2,8]]
n = len(a)

#b = []
#n = len(a)
#for i in range(0,n):
#    b += a[i]
#b.sort()
#"BruteForce sort"
#print b
#print

print a
divide(a,0,n-1)
#conquer(a,0,2,4)
print a

