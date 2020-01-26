class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class SegTree(object):
    def __init__(self, nums):
        self.root = self._buildSegTree(nums, 0, len(nums)-1)
        self.nums = nums
    
    def _buildSegTree(self, nums, l, r):
        val = [l, r, sum(nums[l:r+1])]
        root = TreeNode(val)
        
        if l == r:
            return root
        
        m = (l + r) / 2
        root.left = self._buildSegTree(nums, l, m)
        root.right = self._buildSegTree(nums, m+1, r)
        
        return root
    
    def _traverse(self, root):
        if not root:
            return
        print (root.val)
        self._traverse(root.left)
        self._traverse(root.right)
    
    def update(self, i, new_val):
        node = self.root
        old_val = self.nums[i]
        
        while node:
            l,r,sum_ = node.val
            sum_ = sum_ - old_val + new_val
            node.val[2] = sum_
            
            m = (l + r) // 2
            if i > m:
                node = node.right
            else:
                node = node.left

    
nums = [10,20,30,40,50]
ob = SegTree(nums)
#ob._traverse(ob.root)
ob.update(3, 20)
print("\n\nAfter update")
ob._traverse(ob.root)