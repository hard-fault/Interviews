#Find sets of number that add up to a given value.
#For example - a = [2,4,6,10], value=16 then output= 2 Because {10,4,2} and {10,6}
mem = {}

def rec(a,total,i):
    if total == 0:
        return 1
    elif total < 0:
        return 0
    elif i < 0:
        return 0
    elif total < a[i]:
        return rec(a,total,i-1)
    else:
        return rec(a,total-a[i],i-1) + rec(a,total,i-1)

def dp(a,total,i,mem):
    key = str(total) + ":" + str(i)
    if key in mem:
        return mem[key]
    if total == 0:
        return 1
    elif total < 0:
        return 0
    elif i < 0:
        return 0
    #elif total < a[i]:
    #    ret_val = dp(a,total,i-1,mem)
    ret_val = dp(a,total-a[i],i-1,mem) + dp(a,total,i-1,mem)
    mem[key] = ret_val
    return ret_val

a = [2,4,6,10,1,3,5]
total = 6
print rec(a,total,len(a)-1)

print dp(a,total,len(a)-1,mem)

