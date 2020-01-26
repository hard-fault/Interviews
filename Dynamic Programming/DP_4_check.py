#Find the largest sum subarray {easy}
#i/p: [-2,-3,-4,-1,-5]
#o/p: -1

maxi = []
def rec(a,i):
    if i < len(a):
        sum_value = {True:a[i-1],False:0} [a[i-1] > 0] + a[i]
        maxi.append(sum_value)
        #if sum_value > maxi:
        #    maxi = sum_value
        rec(a,i+1)

a = [-2,1,-3,4,-1,2,1,-5,4]
a = [1,2,8,1,-1000,2,3,4,4,-1,5,6,7]
a =  [-2,-3,-4,-1,-5]
print rec(a,1)
print maxi
