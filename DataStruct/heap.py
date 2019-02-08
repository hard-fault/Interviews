def heapify(nums,i):
    root = i
    left = 2*i + 1
    right = 2*i + 2

    if left < len(nums) and nums[left] < nums[root]:
        root = left
    if right < len(nums) and nums[right] < nums[root]:
        root = right
    
    if root != i:
        nums[i],nums[root] = nums[root],nums[i]
        heapify(nums,root)
    
##Take any array
nums = [4,2,0,3,1,-3,6,7,-23]

## Create a min heap by visitng all the nodes that have children.
for i in range(len(nums)/2 -1,-1,-1):
    heapify(nums,i)
print (nums)

## Heapsort. Pop the root node and heapify.
while nums:
    print (nums[0])
    nums[0] = nums[len(nums)-1]
    nums.pop()
    heapify(nums,0)