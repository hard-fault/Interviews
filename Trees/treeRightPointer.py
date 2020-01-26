class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        self.next = None

##assign node.next to it's level order successor
q = []
def link(root,level,count):
    if root is None:
        return
    q.append([root.left,level+1])
    q.append([root.right,level+1])
    count += 1
    print "linking {} {}".format(root.val,count)
    
    if len(q) > 0:
        node = q.pop(0)
        if count == pow(2,level):
            root.next = None
            count = 0
        else:
            #print "linking {}'s next with {}".format(root.val,q[0].val)
            root.next =  node[0]
        link(node[0],node[1],count)

##assign node.next to it's inorder successor
prev = [None]
def connectInorder(root):
    if root == None:
        return
    connectInorder(root.right)
    if prev[0]:
        print "assigning {}'s next to {}".format(root.val, prev[0].val)
    else:
        print "assigning {}'s next to None".format(root.val)
    root.next = prev.pop(0)
    prev.append(root)
    connectInorder(root.left)

root = TreeNode(10)
root.left = TreeNode(20)
root.right = TreeNode(40)
root.left.left = TreeNode(30)
root.left.right = TreeNode(25)
root.right.left = TreeNode(45)
root.right.right = TreeNode(50)


#link(root,0,0)
# print root.left.next.val
# print root.right.left.next.val

connectInorder(root)
print root.left.left.next.val ##20
print root.left.next.val ##25
print root.left.right.next.val ##10
