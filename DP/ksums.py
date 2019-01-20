def twoSums(a, sum):
    hashTable = {}
    solution = []
    for i in range(len(a)):
        if a[i] in hashTable:
            solution.append([sum - a[i], a[i]])
        else:
            hashTable[sum - a[i]] = 1
    return solution


def threeSums(a, sum):
    hashTable = {}
    solution = []
    for i in range(len(a)):
        partSum = sum - a[i]
        hashTable[partSum] = 1
        for j in range(i+1, len(a)):
            if (a[i] + a[j]) in hashTable:
                solution.append([sum-(a[i]+a[j]), a[i], a[j]])
    return solution

def kSums(a, i, sum):
    if i >= len(a):
        return 0
    if sum == 0:
        return 1
    if a[i] > sum:
        return kSums(a,i+1,sum)
    else:
        return kSums(a,i+1,sum-a[i]) + kSums(a,i+1,sum)

a = [0,1,2,3,4,5,6]
sum = 6
print twoSums(a,sum)

a = [0,1,2,3,4,5,6]
sum = 7
#a = [3,2,-5,-2,0,1,-1]
#sum = 0
print threeSums(a,sum)


a = [1,2,3,4,5,6]
sum = 6
print
print kSums(a,0,sum)
