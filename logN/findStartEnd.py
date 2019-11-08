def findStart(a, lo, hi, key):
    if lo > hi:
        return -1

    mid = ( lo + hi ) / 2
    if key <= a[mid]:
        hi = mid
    elif key > a[mid]:
        lo = mid + 1
    if lo == hi:
        return lo
    return findStart(a, lo, hi, key)

def findEnd(a, lo, hi, key):
    if lo > hi:
        return -1
    mid = ( lo + hi ) / 2
    if key < a[mid]:
        hi = mid
    elif key >= a[mid]:
        lo = mid + 1
    if lo == hi:
        return lo
        
    return findEnd(a, lo, hi, key)

a = [2,2,2,2,2,2,2,2,2,2]
key = 2

print (findStart(a, 0, len(a)-1, key))
print (findEnd(a, 0, len(a)-1, key))