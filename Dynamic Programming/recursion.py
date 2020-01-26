functionCalls = []
def printRecursive(count,index):
    #functionCalls.append(count)
    if count >= 5:
        print "rejecting {}".format(count)
        return
    
    #print functionCalls
    print
    print "{} called me. I am {}".format(count,count+1)
    count += 1
    
    for i in range(index, 5):
        print "enumerating {}'s index{}".format(count, i)
        printRecursive(count,i+1)
    #print "this function        -> {}".format(count)

a = [1,2,3]#,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

printRecursive(0,0)
