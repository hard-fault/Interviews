



a = [3, 2, -5, -2, 0, 1, -1]

list
for i in range(len(a)):
    for j in range(i+1, len(a)):
        num = -(a[i] + a[j])
        if num in dict:
            print "{} {} {}".format(a[i],a[j],num)
        else:
            dict[a[j]] = 1



