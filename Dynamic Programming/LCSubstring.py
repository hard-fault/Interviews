str1 = "OldSite:GeeksforGeeks.org"
str2 = "NewSite:GeeksQuiz.com"

len1 = len(str1)
len2 = len(str2)

"""
let str1 be in coloumns and str2 be in rows
 str2--->
s
t
r
1
|
|
"""

dp =  []*(len1+1)
for i in range(len1+1):
    dp.append([0]*(len2+1))

maxi = -1

for i in range(1, len1+1):
    for j in range(1, len2+1):
        if str1[i - 1] == str2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        if dp[i][j] > maxi:
            maxi = dp[i][j]

print
print maxi
print
for i in dp:
    print
    print i,

