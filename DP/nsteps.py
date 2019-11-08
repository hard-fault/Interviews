def getKsol(k):
    arr = [1]
    
    return arr


def getCombi(n, k):
    arr = getKsol(k)
    i = len(arr)
    while i <= n:
        for j in range(1,k+1):
            temp += arr[-k]
        arr.append(temp)
        i += 1
    return arr[-1]

#print solution(4)