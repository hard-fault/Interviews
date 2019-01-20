def threeProd(a,i):
    if i == len(a)-1:
        return a[i]

    x = threeProd(a,i+1)
    print x
    return x




a = [1,8,5,2,4,3]
print "Array: {}".format(a)
threeProd(a,0)
