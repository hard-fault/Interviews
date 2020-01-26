t = input()
i = 1
while i <= t:
    n = raw_input()
    first = list(n)
    second = list(n)
    for j in range(len(first)):
        if first[j] == '4':
            first[j] = '3'   
            second[j] = '1'  
        else:
            second[j] = '0'
        
    first = int("".join(first))
    second = int("".join(second))
    print ("Case #{}: {} {}".format(i, first, second))
    i +=1