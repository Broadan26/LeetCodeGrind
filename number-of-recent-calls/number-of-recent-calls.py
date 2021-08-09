from typing import Deque

class RecentCounter:

    def __init__(self):
        self.counter = []
        self.window = Deque()

    def pingBrute(self, t: int) -> int:
        pings = 0
        self.counter.append(t)
        for i in range(len(self.counter), 0, -1):
            if t - 3000 <= self.counter[i-1]:
                pings += 1
            else:
                break
        return pings

    def ping(self, t: int) -> int:
        self.window.append(t)
        while self.window[0] < t - 3000:
            self.window.popleft()
        return len(self.window)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
