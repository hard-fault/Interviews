def binarySearch(a,key,lo,hi):
    if lo > hi:
        return -1
    mid = (lo+hi)/2
    if key > a[mid]:
        return binarySearch(a,key,mid+1,hi)
    elif key < a[mid]:
        return binarySearch(a,key,lo,mid)
    else:
        return mid


##Finding the closest element to any given key in a sorted array
def findClosest(a,lo,hi,key):
    if lo < hi:
        mid = (lo+hi)/ 2
        if a[mid] > key:
            return findLow(a,lo,mid-1,key)
        elif a[mid] < key:
            return findLow(a,mid+1,hi,key)
        else:
            return mid
    return lo

##Finding the pivot of a sorted rotated array in O(log n) time.
def old_findPivot(a, lo, hi):
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

def findPivot(a, lo, hi):
    if lo <= hi:
        mid = (lo + hi) / 2
        if (a[mid] < a[lo]):
            return findPivot(a, lo, mid)
        elif (a[mid] > a[hi]):
            return findPivot(a, mid+1, hi)
        else:
            return lo

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


print("\n\n***")
print("Binary search")
print("***")
a = [1,2,4,8,10,11,12,16,18,23,26,29,32,41,44,49,62,83]
a = [1,1,2,2,2,2,2,2,2,2,2,2,3,4,5,6,7,8,9]
key = 2
print (list(enumerate(a)))
print (binarySearch(a,key,0,len(a)))

print("\n\n***")
print ("Rotated sorted array")
print("***")
a = [6,6,6,6,6,6,6,6,7,8,9,10,11,2,3,4,5,5,5,5,5,5,5]
print (list(enumerate(a)))
key = 4
print ("Finding the pivot")
print (findPivot(a,0,len(a)-1))

print ("Search in sorted array")
print (searchRotated(a,0,len(a)-1,key))

print("\n\n***")
print("Find the closest element to the target")
print("***")
a = [10,20,20,30,30,30,40,50,60,60,60,60,70,80,90,100]
key = 69
# print ("Printing the closest element")
# print (findClosest(a, 0, len(a)-1, key))