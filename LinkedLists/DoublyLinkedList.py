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

if __name__ == "__main__":
    main()
        