class TreeNode(object):
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None


class Tree(object):
    def insertBST(self, root, val):
        if root == None:
            node = TreeNode(val)
            root = node

        elif val > root.val:
            root.right = self.insertBST(root.right,val)
        elif val < root.val:
            root.left = self.insertBST(root.left,val)        
        return root
    
    def inorderBST(self,root):
        if root == None:
            return
        self.inorderBST(root.left)
        print(root.val)
        self.inorderBST(root.right)


obj = Tree()
root = TreeNode(30)
obj.insertBST(root, 20)
obj.insertBST(root, 50)
obj.insertBST(root, 85)
obj.insertBST(root, 99)
obj.insertBST(root, 10)
obj.insertBST(root, 3)
obj.insertBST(root, 12)

obj.inorderBST(root)
