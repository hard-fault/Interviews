str1 = "aabcdef"
str2 = "acdfg"

len1 = len(str1)
len2 = len(str2)

dp = []*(len1+1)
for i in range(len1+1):
    dp.append([0]*(len2+1))

maxi = -1
index_i = 0
index_j = 0

for i in range(1,len1 + 1):
    for j in range(1,len2 + 1):
        if str1[i-1] == str2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        if dp[i][j] > maxi:
            index_i = i
            index_j = j
            maxi = dp[i][j]

print maxi

i = index_i
j = index_j

print "max found at {} {}".format(i,j)
subseq = ""

while i >= 0 and j >= 0:
    if dp[i][j] > dp[i-1][j] and dp[i][j] > dp[i][j-1]:
        subseq += str1[i-1]
        i = i - 1
        j = j - 1
    elif dp[i][j] == dp[i-1][j]:
        i = i - 1
    elif dp[i][j] == dp[i][j-1]:
        j = j - 1



print str1
print str2
print subseq[::-1]
