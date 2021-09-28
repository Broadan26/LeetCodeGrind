class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        self.stack_bit = 1 #1 = everything in stack1, 0 = everything in stack2

    def push(self, x: int) -> None:
        '''
        Pushes values on to the stacks
        '''
        if self.stack_bit == 1:
            self.stack1.append(x)
        else:
            while self.stack2:
                self.stack1.append(self.stack2.pop())
            self.stack1.append(x)
            self.stack_bit = 1

    def pop(self) -> int:
        '''
        Pops the values from the stack in FIFO fashion
        '''
        if self.stack_bit == 1:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            self.stack_bit = 0
            return self.stack2.pop()
        else:
            return self.stack2.pop()

    def peek(self) -> int:
        if self.stack_bit == 1:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            self.stack_bit = 0
            return self.stack2[len(self.stack2)-1]
        else:
            return self.stack2[len(self.stack2)-1]

    def empty(self) -> bool:
        '''
        Returns true if stack is empty, false otherwise
        '''
        if self.stack_bit == 1:
            return len(self.stack1) == 0
        else:
            return len(self.stack2) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()