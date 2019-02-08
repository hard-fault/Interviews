#Print all the possible subsets of a given set.
#For example for [1,2] -> {}, {1}, {2}, {1,2}


def getList(subset):
    temp = []
    for s in subset:
        if s != None:
            temp.append(s)
    return temp

all_subsets = []

def rec(a,subset,i):
    if i == len(a):
        print subset
        all_subsets.append(getList(subset))
    else:
        subset[i] = None
        rec(a,subset,i+1)
        subset[i] = a[i]
        rec(a,subset,i+1)

a = [1,2,3]
subset = [None]*len(a)
rec(a,subset,0)
#print all_subsets

