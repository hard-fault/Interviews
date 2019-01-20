"""
If an index i is included, don't include i+1 hence recurse to i+2
"""

def rec(a,subset,i):
    if i >= len(a):
        print sum(subset)
    else:
        subset[i] = a[i]
        rec(a,subset,i+2)
        subset[i] = 0
        rec(a,subset,i+1)


a = [1,2,3,4]
n = len(a)
subset = [0]*n
rec(a,subset,0)