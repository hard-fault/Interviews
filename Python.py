

a = [[0, 30],[15, 20], [5, 10],[190,23],[8,30]]

myDict = {}

for i in range(len(a)):
    myDict[a[i][0]] = a[i][1]

print myDict

print sorted(myDict.iterkeys())

print sorted(myDict.iteritems(), key=lambda (k,v):(v,k))
