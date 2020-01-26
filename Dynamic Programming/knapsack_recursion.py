#Knapsack problem using recursion. Without memoization / DP.
#Try printing the items included in the optimal solution.


def rec(a,i,w,vol):
    if i == 0:
        return 0

    if a[i]["w"] > w or a[i]["vol"] > vol:
        print i
        return  rec(a, i - 1, w, vol)

    return maxi(rec(a, i - 1, w, vol), a[i]["v"] + rec(a, i - 1, w - a[i]["w"], vol - a[i]["vol"]))

def maxi(a,b):
    if a > b:
        return a
    else:
        return b

a = {
1:{"v":1,"w":1, "vol":4},
2:{"v":6,"w":2, "vol":2},
3:{"v":18,"w":5, "vol":15},
4:{"v":22,"w":6, "vol":5},
5:{"v":28,"w":7, "vol":10},
}

w = 11
vol = 19
n = len(a)

print rec(a, n, w, vol)
