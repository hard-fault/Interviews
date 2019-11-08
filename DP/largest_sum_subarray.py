#Find the largest sum subarray {easy}
#i/p: [-2,-3,-4,-1,-5]
#o/p: -1


def kadanesAlgorithm(arr):
    maxSum, currSum = -float('inf'), 0
    for i in range(len(arr)):
        currSum = max (arr[i], currSum+arr[i])
        maxSum = max(currSum, maxSum)
    return maxSum

def kadanesAlgorithmDP(arr):
    mem = [0] * len(arr)
    maxSum = -float('inf')
    mem[0] = arr[0]
    maxSum = max(maxSum, mem[0])

    for i in range(1, len(arr)):
        if mem[i - 1] > 0:
            mem[i] = mem[i - 1] + arr[i]
        else:
            mem[i] = arr[i]
        maxSum = max(maxSum, mem[i])
    return maxSum

a = [-2,-3,-4,1,-5, 2,3]
# a = [-2,1,-3,5,-1,2,1,-5,14]
# a = [-2,-3,-4,-1,-5]
# a = [1,2]

print kadanesAlgorithm(a)
print kadanesAlgorithmDP(a)