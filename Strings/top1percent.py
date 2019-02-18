import heapq

class MaxHeapObj(object):
    def __init__(self,val): self.val = val
    def __lt__(self,other): return self.val > other.val
    def __eq__(self,other): return self.val == other.val
    def __str__(self): return str(self.val)
  

def getTop1percent(words, percent):
    #calculate the percentage
    n = len(words)
    k = 1.0*percent/n * 100
    kHeap = []

    #Parse through the words and insert them into the maxHeap
    for word in words:
        #By default python heaps are minHeaps use this small hack to make the min heap work as a maxHeap
        heapq.heappush(kHeap, MaxHeapObj(word))

        #if the maxHeap is greater then k, then pop out the minimum, only keeping the top k% in heap
        if len(kHeap) > int(k):
            heapq.heappop(kHeap)

    for obj in kHeap:
        print obj.val,


words = ["abc","def","aab","abbc","mno","pqr","uvw","qqr","zzu","mno","aaaabc","bbdd","aaqc","azxy","az","a","mmn","bzc","caa","mno"]

getTop1percent(words,1)