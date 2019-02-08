#Find the largest sum subarray {easy}
#i/p: [-2,-3,-4,-1,-5]
#o/p: -1


a = [-2,-3,-4,1,-5, 2,3]
#a = [-2,1,-3,4,-1,2,1,-5,4]
#a = [1,2]
mem = [0]*len(a)
max_sum = -10000
mem[0] = a[0]
for i in range(1,len(a)):
    if mem[i-1] > 0:
        mem[i] = mem[i-1] + a[i]
    else:
        mem[i] = a[i]
    if mem[i] > max_sum:
        max_sum = mem[i]

print max_sum

