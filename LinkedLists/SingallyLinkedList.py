class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def InsertAtBeginning(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def InsertAtEnd(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node

    def InsertAtPosition(self, val, pos):
        if pos == 1:
            self.InsertAtBeginning(val)
            return
        new_node = Node(val)
        current_pos = 1
        temp = self.head
        while current_pos < pos-1:
            temp = temp.next
            current_pos += 1
        new_node.next = temp.next
        temp.next = new_node
    
    def DeleteFromStart(self):
        self.head = self.head.next

    def DeleteFromEnd(self):
        temp = self.head
        temp2 = temp.next

        while temp2.next is not None:
            temp2 = temp2.next
            temp = temp.next
        
        temp.next = None

    def DeleteFromPosition(self,pos):
        temp = self.head
        current_pos = 1
        while current_pos < pos-1:
            temp = temp.next
            current_pos += 1
        
        temp.next = temp.next.next

    def reverseLinkedList(self):
        if self.head is None:
            return

        if self.head.next is None:
            return

        curr = self.head
        prev = None

        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        self.head = prev

    def printList(self):
        temp = self.head
        while temp is not None:
            print(temp.data,"-> ", end="")
            temp = temp.next
        print("None")

new_list = LinkedList()
for i in range(5,2,-1):
    new_list.InsertAtBeginning(i)
new_list.printList()

for i in range(0,3):
    new_list.InsertAtEnd(i)
new_list.printList()

new_list.InsertAtPosition(10,4)
new_list.printList()

new_list.DeleteFromPosition(4)
new_list.printList()

new_list.DeleteFromStart()
new_list.printList()

new_list.DeleteFromEnd()
new_list.printList()

new_list.reverseLinkedList()
new_list.printList()
