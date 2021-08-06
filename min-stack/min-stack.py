class NodeList:
    def __init__(self, val: int):
        self.next = None
        self.val = val

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minVal = None
        self.toplist = None

    def push(self, val: int) -> None:
        '''
        Pushes a new node to the stack
        '''
        node = NodeList(val)
        if self.toplist is None: #If stack has no nodes
            self.toplist = node
            self.minVal = NodeList(val)
        else: #If stack has nodes already
            node.next = self.toplist
            self.toplist = node
            if self.minVal.val >= node.val: #New node is less than previous min
                temp = self.minVal
                self.minVal = NodeList(val)
                self.minVal.next = temp
        return

    def pop(self) -> None:
        '''
        Removes the top node from the stack
        '''
        if self.toplist: #Stack exists
            if self.toplist.val == self.getMin():
                self.minVal = self.minVal.next
            self.toplist = self.toplist.next
        else: #No stack currently
            print('No stack to pop from')
        return

    def top(self) -> int:
        '''
        Returns the value of the top node in the stack as int
        '''
        if self.toplist: #Stack exists
            return self.toplist.val
        else: #No stack currently
            return None

    def getMin(self) -> int:
        '''
        Returns the minimum value in the stack
        '''
        if self.toplist: #Stack exists
            return self.minVal.val
        else: #No stack currently
            return None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()