class MyStack:

    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        '''
        Pops the elements from the queue
        Expensive pop
        '''
        while len(self.q1) > 1:
            self.q2.append(self.q1.pop(0))
        val = self.q1.pop(0)
        while self.q2:
            self.q1.append(self.q2.pop(0))
        return val

    def top(self) -> int:
        '''
        Shows the top element of the queue
        Expensive top
        '''
        while len(self.q1) > 1:
            self.q2.append(self.q1.pop(0))
        val = self.q1.pop(0)
        while self.q2:
            self.q1.append(self.q2.pop(0))
        self.q1.append(val)
        return val

    def empty(self) -> bool:
        '''
        Returns true if queue is empty, false otherwise
        '''
        return len(self.q1) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()