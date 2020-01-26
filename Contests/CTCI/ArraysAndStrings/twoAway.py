def stringCheck(s1, s2, k):
    s1 = list(s1)
    s2 = list(s2)
    diff = abs(len(s1) - len(s2))
	
    if diff > k:
        return False
	
    if s1 == s2 or s1 in s2 or s2 in s1:
        return True

    err = 0
    while(s1 != [] and s2 != []):
        if s1.pop(0) == s2.pop(0):
            continue
        else:
            err += 1

    if err > k:
        return False
    elif err == k and (s1 != [] or s2 != []):
        return False
    else:
        return True

s1 = "abc"
s2 = "abdd"
print stringCheck(s1,s2,2)

s1 = "abcd"
s2 = "acd"
print stringCheck(s1,s2,3)

s1 = "abc"
s2 = "abcdefgh"
print stringCheck(s1,s2,5)