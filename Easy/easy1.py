#Given an array of 0s and 1s find the 'm' indices which can be swapped to get a longest sequence of 1s
#Ex: a = [1,0,1,0,0] and m = 1 o/p: [1]

a = [1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1]
m = 2
n = len(a)
sub_array = [0] * n
length_max = -1
indices = []
for i in range(n):
    for j in range(i,n):
        sub_array = a[i:j+1]
        zeros = 0
        for s in sub_array:
            if s == 0:
                zeros += 1
        if zeros == m:
            length = len(sub_array)
            if length_max < length:
                indices = []
                length_max = length
                for s in range(0,len(sub_array)):
                    if sub_array[s] == 0:
                        indices.append(s+i)

print indices




