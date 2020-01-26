import sys

class Node:
    def __init__ (self,val):
        self.val = val
        self.next = None
    def traverse (self):
        node = self
        while node != None:
            print node.val
            node = node.next

n = input("Enter number of linked list elements\n")
node_list = []

for i in range(0,n):
    val = input("Enter value_{} - ".format(i+1))
    node = Node(val)
    if i
    node_list.append(node)

for i in range(0,len(node_list)-1):
    node = node_list[i]
    node.next = node_list[i+1]

node_list[n-1].next = None
node_head = node_list[0]

node = node_head
flag = True

while flag == True:
    if node.next == None:
        sys.stdout.write("{}\n".format(node.val))
        flag = False
    else:
        sys.stdout.write("{}->".format(node.val))
        node = node.next

node_head.traverse()
#print node_list


