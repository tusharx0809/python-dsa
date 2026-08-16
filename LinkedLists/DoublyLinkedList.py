"""Double Linked List"""

class Node:
    def __init__(self,val: int):
        self.val = val
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBeginning(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def insertAtEnd(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next

        new_node.prev = temp
        temp.next = new_node

    def insertAtPosition(self, val, pos):
        new_node = Node(val)
        if pos == 1:
            self.insertAtBeginning(val)

        current_pos = 1
        temp = self.head
        while current_pos < pos-1:
            temp = temp.next
            current_pos += 1

        new_node.next = temp.next
        new_node.prev = temp
        temp.next.next.prev = new_node
        temp.next = new_node

    def deleteFromBeginning(self):
        if self.head is None:
            return

        self.head = self.head.next
        self.head.prev = None

    def deleteFromEnd(self):
        if self.head is None:
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.prev.next = None
        temp.prev = None

    def deleteFromPosition(self,pos):
        if self.head is None:
            return

        current_pos = 1
        temp = self.head
        while current_pos < pos - 1:
            temp = temp.next
            current_pos += 1

        temp.next.prev = temp
        temp.next = temp.next.next

    def printList(self):
        temp = self.head
        if temp is None:
            print("None")
            return
        print("None <-> ", end="")
        while temp is not None:
            print(temp.val,"<-> ", end="")
            temp = temp.next
        print("None")

def main():
    linked_list = LinkedList()
    for i in range(0,5):
        linked_list.insertAtBeginning(i)
    linked_list.printList()

    linked_list.insertAtEnd(10)
    linked_list.printList()

    linked_list.insertAtPosition(12,3)
    linked_list.printList()

    linked_list.deleteFromBeginning()
    linked_list.printList()

    linked_list.deleteFromEnd()
    linked_list.printList()

    linked_list.deleteFromPosition(3)
    linked_list.printList()
if __name__ == "__main__":
    main()
        