def sortRec(a, n, i):
    if i >= n:
        return arr

    for j in range(i+1, len(a)):
        if a[j] < a[i]:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp

    return sortRec(arr, n, i+1)

arr = [5,4,3,2,1]

print sortRec(arr, len(arr), 0)


