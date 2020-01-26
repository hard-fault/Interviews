#Print all the possible subsets of a given set.
#For example for [1,2] -> {}, {1}, {2}, {1,2}

class HousePaint:
    def __init__(self):
        self.minSum = float("inf")
        self.all_subsets = []

    def rec(self, a,subset,i):
        if i == len(a):
            self.all_subsets.append(subset)
            subsetSum = sum(x[0] for x in subset)
            if subsetSum < self.minSum:
                prev = subset[1][1][0]
                for x in subset:
                    print x[1],
                print subsetSum
                self.minSum = subsetSum
            
        else:
            for j in range(len(a[i])):
                subset[i] = [a[i][j], [i,j]]
                self.rec(a,subset,i+1)

a = [[5,1,3],[4,2,6],[9,3,9]]
hp = HousePaint()
subset = [None]*len(a)
hp.rec(a,subset,0)
print hp.minSum

