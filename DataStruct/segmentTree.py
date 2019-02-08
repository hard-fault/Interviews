import math
class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def buildSegmentTree(segTree,a,low,high,pos):
    if low == high:
        segTree[pos] = a[low]
        return
    
    mid = (low + high) /2
    buildSegmentTree(segTree,a,low,mid,2*pos+1)
    buildSegmentTree(segTree,a,mid+1,high,2*pos+2)
    segTree[pos] = min(segTree[2*pos+1],segTree[2*pos+2])
    

a = [-1,2,4,0]
n = len(a)
maxLength = pow(2,int(math.ceil(math.log(n,2))))
segTree = [float('inf')]* (maxLength*2 - 1)
print segTree
print a
low = 0
high = n-1
pos = 0
buildSegmentTree(segTree,a,low,high,pos)
print segTree


#inOrder(root)
