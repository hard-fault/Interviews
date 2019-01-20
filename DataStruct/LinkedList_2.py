# A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

# Return a deep copy of the list.



############################################################


# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None


class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


def printLL_Random(head):
    temp = head
    while head!= None:
        print head.label,
        if head.random != None:
            print "[{}], ".format(head.random.label),
        else:
            print "[],",
        head = head.next
    head = temp


def printLL(head):
    temp = head
    while head!= None:
        print head.label,
        head = head.next
    head = temp


def findNode(head, label):
    while head != None:
        if head.label == label:
            return head
        head = head.next
    return None

def copyRandomList(nodeCopy, node, labelList):
    if node == None:
        return None

    if node.label not in labelList:
        nodeCopy.next = RandomListNode(node.label)
        labelList.append(node.label)
    else:
        nodeCopy.next = findNode(head, node.label)

    if node.random == None:
        nodeCopy.next.random = None
    elif node.random.label not in labelList:
        nodeCopy.next.random = RandomListNode(node.random.label)
    else:
        nodeCopy.next.random = findNode(node.random.label)

    copyRandomList(nodeCopy.next, node.next, labelList)


head = RandomListNode(1)
head.next = RandomListNode(2)
head.next.next = RandomListNode(3)
head.next.next.next = RandomListNode(4)
head.next.next.next.next = RandomListNode(5)

head.random = head.next.next
head.next.random = None
head.next.next.random = head.next.next.next
head.next.next.next.random = head.next.next.next.next
head.next.next.next.next.random = None


headCopy = RandomListNode(head.label)
headCopy.random = RandomListNode(head.random.label)
labelList = []
labelList.append(head.label)
labelList.append(head.random.label)
copyRandomList(headCopy, head.next, labelList)
print labelList

print "\nOriginal LL"
printLL(head)
print
printLL_Random(head)


print "\n\nThe deep copy"
printLL(headCopy)
print
printLL_Random(headCopy)


