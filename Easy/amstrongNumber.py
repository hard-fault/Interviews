def getCubeSum(a,b,c,d):
    return (a*a*a) + (b*b*b) + (c*c*c) + (d*d*d)

a = 0
b = 0
c = 0
d = 0
number = 0
numChar = "a"

for a in range(10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                cubeSum = getCubeSum(a,b,c,d)
                numChar = str(a) + str(b) + str(c) + str(d)
                if cubeSum == int(numChar):
                    print int(numChar)


