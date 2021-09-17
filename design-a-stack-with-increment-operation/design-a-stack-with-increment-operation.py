class CustomStack:
    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = []

    def push(self, x: int) -> None:
        '''
        Adds a new element to the stack if stack is less than maxSize
        If stack greater than maxSize, does nothing
        '''
        if len(self.stack) < self.maxSize:
            self.stack.insert(0, x)
        else:
            return None

    def pop(self) -> int:
        '''
        Returns the top value of the stack if it exists
        Returns -1 otherwise
        '''
        if self.stack:
            return self.stack.pop(0)
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        '''
        Integer k indicates the bottom k elements to increase
        Integer val is how much the k elements are increased by
        '''
        if k >= len(self.stack):
            for i in range(0, len(self.stack)):
                self.stack[i] += val
        else:
            for i in range(len(self.stack)-1, len(self.stack)-k-1, -1):
                self.stack[i] += val

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)