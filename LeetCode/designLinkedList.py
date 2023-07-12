class MyLinkedList:
    class Node:
        def __init__(self, val):
            self.val = val
            self.next = None

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        if index >= self.size or index < 0: return -1

        i = 0
        indexedNode = self.head
        while i < index:
            indexedNode = indexedNode.next
            i += 1
        
        return indexedNode.val

    def addAtHead(self, val: int) -> None:
        newNode = self.Node(val)
        if self.size == 0:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.size += 1
        
    def addAtTail(self, val: int) -> None:
        newNode = self.Node(val)
        if self.size == 0:
            self.head = newNode
            self.tail = newNode
        elif self.size == 1:
            self.head.next = newNode
            self.tail = newNode
        else:
           
            self.tail.next = newNode
            self.tail = newNode
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        if index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else:
            newNode = self.Node(val)
            currentNode = self.head
            i = 0
            while i < index - 1:
                currentNode = currentNode.next
                i += 1
            newNode.next = currentNode.next
            currentNode.next = newNode
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        if index == 0:
            if self.size == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
        elif index == self.size - 1:
            if self.size == 1:
                self.head = None
                self.tail = None
            else:
                currentNode = self.head
                while currentNode.next != self.tail:
                    currentNode = currentNode.next
                currentNode.next = None
                self.tail = currentNode
        else:
            currentNode = self.head
            i = 0
            while i < index - 1:
                currentNode = currentNode.next
                i += 1
            currentNode.next = currentNode.next.next
        self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
