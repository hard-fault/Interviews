#Print all the possible subsets of a given set.
#For example for [1,2] -> {}, {1}, {2}, {1,2}


def getList(subset):
    temp = []
    for s in subset:
        if s != None:
            temp.append(s)
    return temp

all_subsets = []

#Using recursion and some crude logic (CS Dojo)
def rec(a,subset,i):
    if i == len(a):
        print subset
        all_subsets.append(getList(subset))
    else:
        subset[i] = None
        rec(a,subset,i+1)
        subset[i] = a[i]
        rec(a,subset,i+1)

##Simple and fast
def subsets(self, nums):
    result = [[]]
    for num in nums:
        result += [i + [num] for i in result]
    return result

##Using DFS
def getSubsets(self, nums, index, path, result):
    result.append(path)
    for i in range(index, len(nums)):
        getSubsets(nums, i+1, path+[nums[i]], result)
        
a = [1,2,3]
subset = [None]*len(a)
rec(a,subset,0)
#print all_subsets

