class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head_node = None

    def traverse (self):
        node = self.head_node
        while node != None:
            print node.val
            node = node.next

    def insertion(self, val):
        new_node = Node(val)
        node = self.head_node
        while node.next != None:
            node = node.next
        node.next = new_node
        new_node.next = None

    def delete(self):
        node = self.head_node
        while (node.next).next != None:
            node = node.next
        node.next = None

    def front_back_split(self, source, frontRef, backRef):
        fast = Node(-1)
        slow = Node(-1)

        slow = source
        fast = source.next
        while fast == None:
            fast = fast.next
            if fast != None:
                slow = slow.next
                fast = fast.next
        frontRef = source
        backRef = slow.next
        slow.next = None


    def sorted_merge(self, a, b):
        result = Node(-1)

        if a.val == -1:
            return b
        elif b.val == -1:
            return a

        if a.val <= b.val:
            result = a
            result.next = sorted_merge(a.next,b)

        else:
            result = b
            result.next = sorted_merge(a,b.next)

        return result

    def merge_sort(self,head_node):
        head = head_node
        a = Node(-1)
        b = Node(-1)

        if head == None or head.next == None:
            return

        self.front_back_split(head,a,b)

        self.merge_sort(a)
        self.merge_sort(b)

        head = self.sorted_merge(a,b)






#Create linked list nodes (load the values, connect the nodes)
head_node = Node(30)
node_2 = Node(10)
node_3 = Node(50)
node_4 = Node(20)
node_5 = Node(40)

head_node.next = node_2
node_2.next = node_3
node_3.next = node_4
node_4.next = node_5
node_5.next = None

#Load the above list of nodes in the LinkedList structure and make the first node as the head node
list = LinkedList()
list.head_node = head_node

#Print the contents of the LinkedList
print "Linked List"
list.traverse()

#Insert
list.insertion(60)
print "\n\nLinked List after a new node insertion"
list.traverse()

#Delete
list.delete()
print "\n\nLinked List after deletion"
list.traverse()

#Sort
list.merge_sort(list.head_node)
print "\n\nSorted list"
list.traverse()

