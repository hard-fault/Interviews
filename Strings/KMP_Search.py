# Python program for KMP Algorithm 
def KMPSearch(pattern, text): 
    m, n = len(pattern), len(text) 
    lps = getLPS(pattern)
    i = j = 0 
    start = -1
    while i < n and j < m: 
        if pattern[j] == text[i]:
            if start == -1:
                start = i
            i, j = i + 1, j + 1
        else:
            if j != 0:
                j = lps[j-1] 
            else: 
                start = -1
                i += 1
        if j == m: 
            return start
    return -1
            
  
def getLPS(pattern): 
    m = len(pattern)
    lps = [0] * m
    i, j = 0, 1

    while j < m: 
        if pattern[i] == pattern[j]: 
            lps[j] = i + 1
            i, j = i+1, j+1
        elif i != 0:
            i = lps[i - 1]
        else:
            lps[j] = 0
            j += 1
    return lps
  
text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
# text = "aabaabaabaaxaabaabaaa"
# pattern = "aabaabaaa"
print(KMPSearch(pattern, text))