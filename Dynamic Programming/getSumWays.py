from functools import lru_cache

def partition(n):
    @lru_cache(None)
    def helper(n, k):
        if n == 0:
            return 1
        return sum(helper(n - i, i) for i in range(1, min(n, k) + 1))
    return helper(n, n - 1)

class GetWays:
    def __init__(self):
        self.mem = {}
    
    def countWays_rec(self, n, k):
        if (n,k) in self.mem:
            return self.mem[(n,k)]
        
        if n == 0:
            return 1

        ways = 0

        for i in range(1, min(n, k) + 1):
            ways += self.countWays_rec(n - i, i) #To create partitions in non-increasing order.
        
        self.mem[(n,k)] = ways
        return ways
    def finalCount(self, target):
        dp = [0] * (target+1)
        dp[0] = 1
        for num in range(1, target):
            for t in range(1, target+1):
                if t - num >= 0:
                    dp[t] += dp[t-num]
        return dp[-1]

    def countWays_dp(self, n): 
        table = [0] * (n + 1)
        table[0] = 1
        for i in range(1, n):
            for j in range(i , n + 1):
                table[j] +=  table[j - i]
        return table[n]
    
    def countWays_dpTable(self,n):
        dpTable = [[0 for _ in range(n+1)] for _ in range(n)]
        for i in range(n):
            dpTable[i][0] = 1
        
        for i in range(1, n):
            for j in range(1, n+1):
                dpTable[i][j] = dpTable[i-1][j]
                if j >= i:
                    dpTable[i][j] += dpTable[i][j-i]
        
        return dpTable[-1][-1]


n = 100
ob = GetWays()
print (ob.countWays_rec(n, n-1), ob.countWays_dp(n), ob.countWays_dpTable(n), ob.finalCount(n))