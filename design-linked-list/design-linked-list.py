class ListNode:
    
    def __init__(self, val: int, next : 'ListNode' = None):
        self.val = val
        self.next = next

        
class MyLinkedList:

    def __init__(self, length=0, head=None, tail=None):
        self.length = length
        self.head = head
        self.tail = tail

    def get(self, index: int) -> int:
        '''
        Returns the value of a node at the specified index
        '''
        if index >= self.length: # Invalid index
            return -1

        iterator = self.head
        for _ in range(index):
            iterator = iterator.next
        return iterator.val

    def addAtHead(self, val: int) -> None:
        '''
        Adds a new node to the front of a linked list
        '''
        if self.length == 0:
            self.head = ListNode(val)
            self.tail = self.head
        else:
            new_node = ListNode(val, self.head)
            self.head = new_node
        self.length += 1

    def addAtTail(self, val: int) -> None:
        '''
        Adds a new node to the end of a linked list
        '''
        if self.length == 0:
            self.head = ListNode(val)
            self.tail = self.head
        else:
            new_node = ListNode(val)
            self.tail.next = new_node
            self.tail = self.tail.next
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        '''
        Adds a new node at the specified index
        '''
        if index == 0: # Add to the head
            self.addAtHead(val)
        elif index == self.length: # Add to the tail
            self.addAtTail(val)
        elif index > self.length:
            print('Cannot insert at given index')
        else:
            iterator = self.head
            for _ in range(index-1):
                iterator = iterator.next
            new_node = ListNode(val, iterator.next)
            iterator.next = new_node
            self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        '''
        Deletes a node at a given index in the linked list
        '''
        if self.length == 0 or index >= self.length: # No list exists
            return

        if index == 0: # Removing the head
            self.head = self.head.next
        elif index == self.length-1: # Removing the tail
            iterator = self.head
            for _ in range(index-1):
                iterator = iterator.next
            iterator.next = None
            self.tail = iterator
        else: # Removing in middle of list
            iterator = self.head
            for _ in range(index-1):
                iterator = iterator.next
            iterator.next = iterator.next.next
        self.length -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)