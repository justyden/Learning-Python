from Node import *


class LinkedList:
    def __init__(self):
        self.head = None
        self.last = None

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            self.last = self.head
        else:
            self.last.next = Node(data)
            self.last = self.last.next

    def printHead(self):
        print(self.head.data)

    def printTail(self):
        print(self.last.data)

    def display(self):
        currentNode = self.head
        while (currentNode is not None):
            print(currentNode.data)
            currentNode = currentNode.next


linkedList1 = LinkedList()
n = 5
for i in range(n):
    data = input("Enter a data value. ")
    linkedList1.append(data)

# linkedList1.printHead()
# linkedList1.printTail()
linkedList1.display()
