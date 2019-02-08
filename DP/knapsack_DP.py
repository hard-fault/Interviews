#Knapsack problem using DP
from collections import defaultdict

def maxi(a,b,c):
    if a > b and a > c:
        return a
    elif b > a and b >c:
        return b
    else:
        return c



values = {}
a = {}

filenames = ["KP_input_1.txt","KP_input_2.txt","KP_input_3.txt"]

for filename in filenames:
    file = open(filename, "r")
    for line in file:
        print l

#for i in range(n):
#    v = raw_in


"""
a = {
1:{"v":1,"w":2},
2:{"v":6,"w":2},
3:{"v":18,"w":5},
4:{"v":22,"w":5},
5:{"v":28,"w":8},
}
W = 10
a = {
1:{"v":15,"w":2},
2:{"v":16,"w":3},
3:{"v":40,"w":4},
4:{"v":29,"w":4},
}
W = 10
"""
itemsIncluded = []

n = len(a)
mem = defaultdict(list)

mem[0] = [0] * (W + 1)
for i in a.keys():
    mem[i] = [0] * (W + 1)

for i in range(1, n + 1):
    for w in range(1,W + 1):
        if a[i]["w"] > w:
            mem[i][w] = mem[i - 1][w]
        else:
            mem[i][w] = maxi(mem[i - 1][w], a[i]["v"] + mem[i - 1][w - a[i]["w"]], a[i]["v"] + mem[i][w - a[i]["w"]])
i = n
w = W
weight = W

while i > 0 and weight > 0:
    while w > 0 and weight > 0:
        if mem[i][w] == mem[i-1][w]:
            i = i - 1
        elif mem[i][w] > mem[i-1][w]:
            itemsIncluded.append(i)
            weight = weight - a[i]["w"]
            w = w - a[i]["w"]
    w = W
    i = i - 1

for i in range(n + 1):
    print mem[i]

print mem[n][W]

print
print
print
print itemsIncluded
