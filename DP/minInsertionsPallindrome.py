
def minInsertions(str,start,end):
    if start >= end:
        return 0
    
    if dpTable[start][end] != -1:
        return dpTable[start][end]

    if str[start] == str[end]:
        dpTable[start][end] =  minInsertions(str, start+1, end-1)
    else:
        dpTable[start][end] =  min(minInsertions(str, start+1,end), minInsertions(str, start, end-1))+1
    
    return dpTable[start][end]


# def minDeletions(str, start, end):
#     if start >= end:
#         return 0
    
#     if str[start] == str[end]:
#         return minDeletions(str, start+1,end-1)
#     else:
#         min()


str = "geeksforgeeks"
dpTable = [[-1 for i in range(len(str))] for i in range(len(str))]
print(minInsertions(str, 0, len(str)-1))

    

    

