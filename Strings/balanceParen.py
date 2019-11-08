def minRemovals(s):
    res = ""
    n = len(s)
    remove = [0] * n
    left = right = 0
    for i in range(n):
        if s[i] == '(':
            left += 1
        elif s[i] == ')':
            left -= 1
        if left < 0:
            remove[i] = 1
    
    for i in range(n-1, -1, -1):
        if s[i] == ')':
            right += 1
        elif s[i] == '(':
            right -= 1
        if right < 0:
            remove[i] = 1
    
    for i in range(n):
        if not remove[i]:
            res += s[i]

    return res

string = "(())))"
print(minRemovals(string))