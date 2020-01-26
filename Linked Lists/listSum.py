import collections

class LinkedListNode:
    def __init__(self,val):
        self.val = val
        self.next = None

class linkedListAPIs:
    def listSum(self,l1,l2):
        l3 = LinkedListNode(0)
        head = l3
        carry = 0
        while l1 != None or l2 != None:
            if l1 == None: lhs = 0
            else: lhs = l1.val
            if l2 == None: rhs = 0
            else: rhs = l2.val
            sum = lhs+rhs+carry
            if sum > 9:
                sum %= 10
                carry = 1
            else: carry = 0
            l3.val = sum
            l3.next = LinkedListNode(0)
            l3 = l3.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        if carry:
            l3.val = carry
        return head

    def printList(self, l):
        while l!= None:
            print l.val,
            l = l.next
        print
    
    def createDict(self,dict,l):
        while l != None:
            if l in dict: dict[l] += 1
            else: dict[l] = 1
            l = l.next
        return dict


l1 = LinkedListNode(1)
l1.next = LinkedListNode(9)
l1.next.next = LinkedListNode(9)

l2 = LinkedListNode(9)
l2.next = LinkedListNode(9)
l2.next.next = LinkedListNode(9)

obj = linkedListAPIs()
obj.printList(l1)
obj.printList(l2)

l3 = obj.listSum(l1,l2)
obj.printList(l3)

##Finding the intersecting node
l1 = LinkedListNode(1)
l1.next = LinkedListNode(9)
l1.next.next = LinkedListNode(9)

l2 = LinkedListNode(9)
l2.next = l1
l2.next.next = LinkedListNode(9)
dict = {}
print obj.createDict(dict,l1)
print obj.createDict(dict,l2)
print collections.Counter(dict).most_common(1)[0][0].val