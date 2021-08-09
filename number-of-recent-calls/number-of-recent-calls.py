class RecentCounter:

    def __init__(self):
        self.counter = []

    def ping(self, t: int) -> int:
        pings = 0
        self.counter.append(t)
        for i in range(len(self.counter), 0, -1):
            if t - 3000 <= self.counter[i-1]:
                pings += 1
            else:
                break
        return pings


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)