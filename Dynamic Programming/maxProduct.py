def maxProduct(a):
    maxProd = -1
    for i in range(0,len(a)):
        for j in range(i+1,len(a)):
            for k in range(j+1,len(a)):
                prod = a[i] * a[j] * a[k]
                maxProd = max(prod, maxProd)
    return maxProd

a = [-7,-7,8,4,7]

print maxProduct(a)