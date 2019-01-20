#Local minima

def rec(a,l,r,n):
    m = (l + r) / 2
    if m == 0 or a[m] < a[m-1] and (m == (n-1)) or a[m] < a[m+1]:
        return a[m]
    elif m > 0 and a[m-1] < a[m]:
        return rec(a,l,m-1,n)
    #elif m > 0 and a[m+1] < a[m]:
    return rec(a,m+1,r,n)

def localMinUtil(arr, low, high, n):

    # Find index of middle element
    mid = low + (high - low) // 2

    # Compare middle element with its
    # neighbours (if neighbours exist)
    if(mid == 0 or arr[mid - 1] > arr[mid] and
       mid == n - 1 or arr[mid] < arr[mid + 1]):
        return arr[mid]

    # If middle element is not minima and its left
    # neighbour is smaller than it, then left half
    # must have a local minima.
    elif(mid > 0 and arr[mid - 1] < arr[mid]):
        return localMinUtil(arr, low, mid - 1, n)

    # If middle element is not minima and its right
    # neighbour is smaller than it, then right half
    # must have a local minima.
    return localMinUtil(arr, mid + 1, high, n)

#a = [15,9,7,6,1,5]
a = [4, 3, 6, 14, 16, 40]
n = len(a)
print rec(a,0,n-1,n)
print localMinUtil(a,0,n-1,n)


