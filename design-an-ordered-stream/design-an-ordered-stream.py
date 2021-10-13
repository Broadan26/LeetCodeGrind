class OrderedStream:

    def __init__(self, n: int):
        self.length = n # Remember the length
        self.stream_list = [' '] * self.length # Create empty list
        self.ptr = 0 # Remember last start location

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream_list[idKey-1] = value # Store val
        answer = []
        for val in range(self.ptr, self.length): # Iterate chunks
            if self.stream_list[val] == ' ':
                break
            else:
                self.ptr += 1
                answer.append(self.stream_list[val])
        return answer # Return chunks

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)