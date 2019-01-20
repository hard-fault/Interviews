a = [8,1,7,3,4,5,9]

max1 = -1
max2 = -1

for i in range(len(a)):
    if i == 0 and a[i] > max1:
        max1 = a[i]

    if i != 0 and a[i] > max1:
        if max1 > max2:
            max2 = max1
        max1 = a[i]

    if i != 0 and a[i] > max2 and a[i] != max1:
        max2 = a[i]

print a
print max1
print max2
