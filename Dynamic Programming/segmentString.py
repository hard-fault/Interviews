
def segmentString(str):
    n = len(str)
    words = []
    for i in range(n):
        for j in range(i,n):
            words.append(str[i:j+1])
    
    return words
            
str = "abcdef"
words = segmentString(str)
print(words)
dict = {"a":1, "b":1,"cd":1,"ef":1}

for i in range(len(words)):
    word = words[i]
    if word in dict:
        for j in range(len(words)):