class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def printInorder(root):
    if root == None:
        return
    printInorder(root.left)
    print root.val,
    printInorder(root.right)

def constructTree(arr, l,h,root):
    if l <= h:
        m = (l+h)/2
        root.val = arr[m]
        if l <= m-1:
            root.left = TreeNode(-1)
            constructTree(arr,l,m-1,root.left)
        if m+1 <= h:
            root.right = TreeNode(-1)
            constructTree(arr,m+1,h,root.right)

def sortedArrayToBST(num):
        if not num:
            return None
        mid = len(num) / 2
        root = TreeNode(num[mid])
        root.left = sortedArrayToBST(num[:mid])
        root.right = sortedArrayToBST(num[mid+1:])
        return root

arr = [1,2,3,4,5,6,7,8,9,10]
root = TreeNode(-1)
constructTree(arr,0,len(arr)-1,root)
printInorder(sortedArrayToBST(arr))
print
printInorder(root)