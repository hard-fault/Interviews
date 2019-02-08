class TrieNode:
    def __init__(self,val):
        self.val = val
        self.children = {}
        self.wordEnd = False
        
class Trie(object):
    def __init__(self):
        self.root = TrieNode('$')

    def insert(self, word):
        curr = self.root
        for w in word:
            if w not in curr.children:
                newNode = TrieNode(w)
                curr.children[w] = newNode
            curr = curr.children[w]            
        curr.wordEnd = True

    def search(self, word):
        curr = self.root
        for w in word:
            if w not in curr.children:
                return False
            curr = curr.children[w]
        if curr.wordEnd:
            return True
        else:
            return False
        
    def startsWith(self, prefix):
        curr = self.root
        for w in prefix:
            if w not in curr.children:
                return False
            curr = curr.children[w]
        return True
        



obj = Trie()
obj.insert("apple")
obj.insert("and")
obj.insert("another")
obj.insert("anotherday")


print obj.search("apple")
print obj.search("and")
print obj.search("anda")
print obj.search("another")
print obj.search("anoterrr")
print obj.search("anotherda")
print obj.search("anotherday")

# prefix = "appd"
# print obj.startsWith(prefix)