class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

mapTree ={}

def indSet1(root):
    if root == None:
        return
    if root.left == None and root.right == None:
        mapTree[root.val] = 1

    indSet1(root.left)
    indSet1(root.right)

def indSet2(root):
    if root == None:
        return
    if root.left != None and root.left.val in mapTree:
        if mapTree[root.left.val] == 1:
            mapTree[root.val] = 0
    elif root.right != None and root.right.val in mapTree:
        if mapTree[root.right.val] == 1:
            mapTree[root.val] = 0
    else:
        mapTree[root.val] = 1

    indSet2(root.left)
    indSet2(root.right)


root = TreeNode(10)
root.left = TreeNode(20)
root.right = TreeNode(30)
root.left.left = TreeNode(40)
root.left.right = TreeNode(50)
root.right.right = TreeNode(60)
root.left.right.left = TreeNode(70)
root.left.right.right = TreeNode(80)

#Including leaves
indSet1(root)

#Including the other nodes
indSet2(root)
print mapTree
