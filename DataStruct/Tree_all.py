# Definition for a binary tree node.
BFS_queue = []
BFS_List = []

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

def BFS(root, visited):
    visited[root] = 1
    BFS_List.append(root.val)

    if root.left != None and root.left not in visited:
        BFS_queue.append(root.left)


    if root.right != None and root.right not in visited:
        BFS_queue.append(root.right)

    if len(BFS_queue) > 0:
        BFS(BFS_queue.pop(0), visited)

##Beware: inefficent implementation (h^2 ~ n^2)
def printLevelOrder(root, level, toggle):
    if root == None:
        return
    if level == 1:
        print root.val,
    elif level > 1:
        if toggle:
            printLevelOrder(root.left, level - 1,toggle)
            printLevelOrder(root.right, level - 1,toggle)
        else:
            printLevelOrder(root.right, level - 1,toggle)
            printLevelOrder(root.left, level - 1,toggle)

def levelOrder(root):
    h = 3
    for i in range(1,h+1):
        print
        printLevelOrder(root,i,1)

##Beware: inefficent implementation (h^2 ~ n^2)
def spiralOrder(root):
    h = 3
    toggle = 0
    for i in range(1,h+1):
        print
        if i % 2 == 0:
            toggle = 1
        else:
            toggle = 0
        printLevelOrder(root,i,toggle)


def findPath(root, path, n):
    if root == None:
        return False

    path.append(root.val)
    if root.val == n:
        return True

    if findPath(root.left, path, n) or findPath(root.right, path, n):
        return True

    path.pop()
    return False

def LCA(root, n1, n2):
    path1 = []
    path2 = []
    findPath(root, path1, n1)
    findPath(root, path2, n2)
    m = min(len(path1),len(path2))
    for i in range(m):
        if path1[i] == path2[i]:
            continue
        else:
            return path1[i-1]
    return path1[i]

def findNode(root, n):
    if root == None:
        return False
    if root.val == n:
        return True
    if findNode(root.left, n) or findNode(root.right, n):
        return True
    return False

def findMaxSumPath(root, max_n):
    if root == None:
        return max_n

    findMaxSumPath(root.left, max_n)
    findMaxSumPath(root.right, max_n)

    if root.val > max_n:
        max_n = root.val
    return max_n

def isMirror(root1, root2):
    if root1 == None and root2 == None:
        return True
    if root1 == None or root2 == None:
        return False

    return (root1.val == root2.val) and isMirror(root1.left, root2.right) and isMirror(root1.right, root2.left)

BFS_Queue = []
##Level order using BFS, (one queue for BFSQueue and the other for the solution).
def levelOrder2(root,level,nodeList):
    if root == None:
        return
    if len(nodeList) == level:
        nodeList.append([])
    nodeList[level].append(root.val)
    BFS_Queue.append([root.left,level+1])
    BFS_Queue.append([root.right,level+1])
    if len(BFS_Queue) != 0:
        node = BFS_Queue.pop(0)
        return levelOrder2(node[0],node[1],nodeList)

##Level order using DFS
def levelOrder1(root,level,nodeList):
    if root == None:
        return
    
    if len(nodeList) == level:
        nodeList.append([])

    nodeList[level].append(root.val)
    
    levelOrder1(root.left,level+1,nodeList)
    levelOrder1(root.right,level+1,nodeList)

##Zigzag order using BFS in O(n)
def zigZagOrder(root,level,nodeList):
    if root == None:
        return
    
    if len(nodeList) == level:
        nodeList.append([])
    
    if level %2 == 0:
        nodeList[level].append(root.val)
    else:
        nodeList[level].insert(0,(root.val))
    
    zigZagOrder(root.left,level+1,nodeList)
    zigZagOrder(root.right,level+1,nodeList)

##diagonal Traversal
diagonalQ = []
def diagonalTraversal(root):
    if root == None:
        return
    print root.val,
    diagonalQ.append(root.left)
    diagonalTraversal(root.left)
    diagonalQ.append(root.right)
    diagonalTraversal(root.right)

##Get maxWidth
leftIndex = {}
def getMaxWidth(root,level, pos):
    if root == None:
        return

    if level not in leftIndex:
        leftIndex[level] = pos
        
    return max(
    getMaxWidth(root.left,level+1, 2*pos+1), 
    getMaxWidth(root.right,level+1, 2*pos+2),
    pos - leftIndex[level] + 1
    )
    

##findIndex
def findIndex(root,index,target):
    if root == None:
        return False
    if index == target:
        return True
    
    leftSide = findIndex(root.left,2*index,target)
    rightSide = findIndex(root.right,2*index+1,target)

    return (leftSide or rightSide)


##Next pointer must point to the inorder successor.
def inorderReverse

root = TreeNode(10)
root.left = TreeNode(20)
root.right = TreeNode(40)
root.left.left = TreeNode(30)
root.left.right = TreeNode(25)
root.right.left = TreeNode(45)
root.right.right = TreeNode(50)
root.left.left.left = TreeNode(29)
root.left.left.right = TreeNode(42)

# ####BFS and LevelOrder####
# print "\n\n***levelOrder2 [O(n)]***"
# toggle = 0
# nodeList = []
# levelOrder1(root,0,nodeList)
# print nodeList

# ####zigZagOrder####
# print "\n\n***zigZag Order***"
# nodeList = []
# zigZagOrder(root,0,nodeList)
# print nodeList

####diagonaTraversal####
# print "\n\n***Diagonal Traversal***"
# diagonalTraversal(root)

####getIndex####
print "\n\n***Nodes with index***"
print findIndex(root,1,0)


# ####getMaxWidth####
# print "\n\n***Max Width***"
# print getMaxWidth(root,0, 0)


# ####FindPath####
# print "\n\n***Path from root to 42***"
# path = []
# findPath(root, path, 42)
# print path

# ####LCA####
# print "\n\n***LCA***"
# print LCA(root,40,50)

# ####find a node####
# print "\n\n***find a node (400)***"
# print findNode(root, 400)
# print "\n\n***find a node (40)***"
# print findNode(root, 40)

# ####find max sum path####
# print "\n\n***max sum path***"
# max_n = -1
# print findMaxSumPath(root, max_n)

# ####check if the tree is symmetric (can also be extended to check if two trees are mirror are of each other)####
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.left = TreeNode(3)
# root.left.right = TreeNode(4)
# root.right.left = TreeNode(4)
# root.right.right = TreeNode(3)

# root2 = TreeNode(1)
# root2.left = TreeNode(2)
# root2.right = TreeNode(3)
# root2.left.left = TreeNode(3)
# root2.left.right = TreeNode(4)
# root2.right.left = TreeNode(4)
# root2.right.right = TreeNode(3)


# print "\n\n***Is tree symmetric***"
# print isMirror(root, root2)


# class TreeNode2:
#     def __init__(self,val):
#         self.val = val
#         self.children = []

# ##Get max length path
# maxPath = [0]

# def getMaxLengthPath(root, pathCount):
#     if root == None: 
#         return 1

#     maxPath[0] = max(pathCount, maxPath[0])

#     print root.val, maxPath[0]
#     for c in root.children:
#         if root.val == c.val:
#             getMaxLengthPath(c, pathCount+1)
#         else:
#             getMaxLengthPath(c, 0)


# root = TreeNode2(10)
# root.children.append(TreeNode2(20))
# root.children.append(TreeNode2(30))
# root.children.append(TreeNode2(40))

# root.children[0].children.append(TreeNode2(20))
# # root.children[1].children.append(TreeNode2(20))
# # root.children[1].children[0].children.append(TreeNode2(20))
# # root.children[1].children[0].children[0].children.append(TreeNode2(20))
# # root.children[1].children[0].children[0].children[0].children.append(TreeNode2(20))

# root.children[2].children.append(TreeNode2(20))
# root.children[2].children.append(TreeNode2(20))
# root.children[2].children[1].children.append(TreeNode2(20))
# root.children[2].children[1].children[0].children.append(TreeNode2(20))

# getMaxLengthPath(root,0)
# print maxPath[0]
