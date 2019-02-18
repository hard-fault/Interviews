def binarySearch(a,key,lo,hi):
    if lo > hi:
        return -1
    mid = (lo+hi)/2
    if lo == hi:
        return lo
    if key >= a[mid]:
        return binarySearch(a,key,mid+1,hi)
    elif key < a[mid]:
        return binarySearch(a,key,lo,mid)

##Finding the closest element to any given key in a sorted array
def findLow(a,lo,hi,key):
    if hi < lo:
        return -1
    if hi == lo:
        return hi
    mid = (lo+hi)/2
    if a[mid] > key:
        return findLow(a,lo,mid-1,key)
    elif a[mid] < key:
        return findLow(a,mid+1,hi,key)

##Finding the pivot of a sorted rotated array in O(log n) time.
def findPivot(a, lo, hi):
    if hi < lo:
        return -1
    if hi == lo:
        return lo
    mid = (hi+lo)/2
    if a[mid] > a[mid+1]:
        return mid
    if a[mid] < a[mid-1]:
        return mid-1
    if a[0] > a[mid]:
        return findPivot(a,lo,mid-1)
    return findPivot(a,mid+1,hi)

##Binary search in a rotated sorted array
def searchRotated(a,lo,hi,key):
    if hi < lo:
        return -1
    mid = (hi+lo)/2

    if a[mid] == key:
        return mid
    
    if a[lo] <= a[mid]:
        if a[lo] <= key <= a[mid]:
            return searchRotated(a, lo, mid-1, key)
        else:
            return searchRotated(a,mid+1, hi, key)
    else:
        if a[mid] <= key <= a[hi]:
            return searchRotated(a, mid+1, hi, key)
        else:
            return searchRotated(a,lo, mid-1, key)



# a = [1,1,2,2,2,2,2,2,2,2,2,2,3,4,5,6,7,8,9]
# key = 2
# print (list(enumerate(a)))
# print (binarySearch(a,key,0,len(a)))

# a = [1,2,4,8,10,11,12,16,18,23,26,29,32,41,44,49,62,83]
# key = 965
# print (findLow(a,0,len(a),key))

a = [6,7,8,9,10,11,2,3,4,5]
key = 4

print (findPivot(a,0,len(a)))
print (searchRotated(a,0,len(a)-1,key))