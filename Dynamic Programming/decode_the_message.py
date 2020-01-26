#DP_2
#a-1, b-2 ... z-26. Given a string of numbers, find the number of messages that can be decoded from it.
#For example: "12" is either "ab" or "l" so the answer is 2.

def rec(a,k):
    if k == 0:
        return 1

    s = len(a) - k

    if a[s] == "0":
        return 0

    result = rec(a,k-1)
    if k >=2 and int(a[s:s+2]) <= 26:
        result += rec(a,k-2)

    return result

a = "2125"
print rec(a,len(a))

