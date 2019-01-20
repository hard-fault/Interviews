#In a contigous sorted array, find the missing element.

a = [1,3,4,5,6,7,8,9]
n = len(a)

start = 0
end = n -1

while (end - start) > 1:
    mid = (start + end) / 2
    if a[start] - start != a[mid] - mid:
        end = mid
    elif a[end] - end != a[mid] - mid:
        start = mid

mid = (start + end)/2

print "The missing element is {}".format(a[mid]+1)
