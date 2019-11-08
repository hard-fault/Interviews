t = input()
i = 1
while i <= t:
    n = input()
    lydia = raw_input()
    result = list(lydia)
    
    for j in range(len(result)):
        if result[j] == "E":
            result[j] = "S"
        elif result[j] == "S":
            result[j] = "E"
    result = "".join(result)
    print ("Case #{}: {}".format(i, result))
    i +=1