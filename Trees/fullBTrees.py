# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class FBT(object):
    def allPossibleFBT(self, N):
        root = TreeNode(0)
        self._buildTree(root, root, 1, N, True)
    
    def _buildTree(self, root, node, leafCount, N, capture):
        if leafCount == N:
            if capture:
                self._printTree(root)
            return
        node.left, node.right = TreeNode(0), TreeNode(0)
        self._buildTree(root, node.left, leafCount-1+2, N, True)
        self._buildTree(root, node.right, leafCount-1+2, N, False)
        node.left, node.right = None, None
    
    def _printTree(self, root):
        if not root:
            return
        
        levelOrder, BFSQueue = [], [(root)]
        while BFSQueue:
            node = BFSQueue.pop(0)
            if node:
                levelOrder.append(node.val)
                BFSQueue.append(node.left)
                BFSQueue.append(node.right)
            else:
                levelOrder.append(None)
        
        print "\n\nTree:\n"
        for idx, node in enumerate(levelOrder):
            print node,"({})".format(idx),


ob = FBT()
ob.allPossibleFBT(5)