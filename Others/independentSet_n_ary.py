class TreeNode:
    def __init__(self, val):
        self.val = val
        self.child = []

mapTree ={}

def indSet1(root):
    if root == None:
        return
    if len(root.child) == 0:
        mapTree[root.val] = 1

    for child in root.child:
        indSet1(child)

def indSet2(root):
    childIncluded = 0
    if root == None:
        return
    for child in root.child:
        if child != None and child.val in mapTree:
            if mapTree[child.val] == 1:
                mapTree[root.val] = 0
                childIncluded = 1
                break
    if childIncluded == 0:
        mapTree[root.val] = 1

    for child in root.child:
        indSet2(child)


root = TreeNode(10)
root.child.append(TreeNode(20))
root.child.append(TreeNode(30))
root.child.append(TreeNode(40))
root.child[0].child.append(TreeNode(50))
root.child[0].child.append(TreeNode(60))
root.child[0].child[1].child.append(TreeNode(110))

root.child[1].child.append(TreeNode(70))
root.child[1].child.append(TreeNode(80))
root.child[1].child.append(TreeNode(90))

root.child[2].child.append(TreeNode(100))


indSet1(root)
#print mapTree

indSet2(root)
#print mapTree

print "Max Indpendent set"
for entry in mapTree:
    if mapTree[entry] == 1:
        print entry,
print
