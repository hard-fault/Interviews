
maxLength = -1

def longestIncreasingSubSeq(a,prev,i):
    if i >= len(a):
        return 0
    global maxLength
    lengthInclusive = 0

    if a[i] > prev:
        lengthInclusive = 1+ longestIncreasingSubSeq(a,a[i],i+1)
    
    lengthNonInculsive = longestIncreasingSubSeq(a,prev,i+1)
    maxLength = max(lengthInclusive,lengthNonInclusive)
    return maxLength

def dpLIS(a,prev,i):
    if i >= len(a):
        return 0
    global maxLength
    lengthInclusive = 0

    if a[i] > prev:
        if dpTable[prev][i+1] != -1:
            return dpTable[prev][i+1]
        else:
            dpTable[prev][i+1] = 1+ longestIncreasingSubSeq(a,a[i],i+1)
    
    if dpTable[prev][i] != -1:
        dpTable[prev][i] = longestIncreasingSubSeq(a,prev,i+1)
        lengthNonInculsive = longestIncreasingSubSeq(a,prev,i+1)
    maxLength = max(lengthInclusive,lengthNonInclusive)
    return maxLength

a = [-1,10,9,2,5,3,7,101,18]
dpTable = [[-1 for i in range(len(a))] for j in range(len(a))]
print dpTable
longestIncreasingSubSeq(a,a[0],1)
print (maxLength)
