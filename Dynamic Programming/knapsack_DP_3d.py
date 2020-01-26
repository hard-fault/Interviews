#Knapsack problem using DP
from collections import defaultdict

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

W = 11
VOL = 19
n = len(a)
mem = defaultdict(list)

mem[0] = [0] * (W + 1)
for i in a.keys():
    mem[i] = [0] * (W + 1)
    for j in a.keys():
        mem[i][j] = [0] * (VOL + 1)

for i in range(1, n + 1):
    for w in range(1,W + 1):
        for v in range(1, VOL + 1):
            if a[i]["w"] > w or a[i]["vol"] > v:
                print mem[i, w, v]
                mem[i, w, v] = mem[i - 1, w, v]
        else:
            mem[i, w, v] = maxi(mem[i - 1, w, v], a[i]["v"] + mem[i - 1, w - a[i]["w"], v - a[i]["vol"]])

for i in range(n + 1):
    print mem[i]

print
print
print mem[n,W,VOL]
