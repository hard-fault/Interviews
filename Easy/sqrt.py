n = 13

perfectSq = 1
count = 1
oddSeq = 3
while perfectSq <= n:
    if perfectSq == n:
        break
    count += 1
    perfectSq += oddSeq
    oddSeq += 2
    
print count