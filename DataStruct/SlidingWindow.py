from collections import deque

"""
Tasks:

Use deque to store the indices. 
[such that index of the largest element in the window is stored in the front and the smallest's in rear]

Inserting:
insert all the indices that belong to a window.

Remove:
1) pop indices from the front that are out of the window.
2) pop indices of the numbers that are smaller than the present number from the rear of the queue. (Note: smaller numbers are in rear)
"""
def slidingWindowMax(nums,k):
    if nums == [] or k == 0 or k > len(nums):
        return []
    
    indexQ = deque()
    resultMax = []
    n = len(nums)

    for i in range(k):
        while indexQ and nums[i] >= nums[indexQ[-1]]:
            indexQ.pop()
        indexQ.append(i)
    
    for i in range(k,n):
        resultMax.append(nums[indexQ[0]])

        while indexQ and indexQ[0] <= i-k:
            indexQ.popleft()
        
        while indexQ and nums[i] >= nums[indexQ[-1]]:
            indexQ.pop()
        
        indexQ.append(i)
    
    resultMax.append(nums[indexQ[0]])

    return resultMax

def slidingWindowMin(nums, k):
    indexQ = deque()
    resultMin = []
    n = len(nums)

    for i in range(k):
        while indexQ and nums[i] <= nums[indexQ[-1]]:
            indexQ.pop()
        indexQ.append(i)
    
    for i in range(k,n):
        resultMin.append(nums[indexQ[0]])
        while indexQ and indexQ[0] <= i-k:
            indexQ.popleft()
        while indexQ and nums[i] <= nums[indexQ[-1]]:
            indexQ.pop()
        indexQ.append(i)
    resultMin.append(nums[indexQ[0]])

    return resultMin



a = [12,1,78,90,57,89,56]
k = 3
print (slidingWindowMax(a,k))
print (slidingWindowMin(a,k))