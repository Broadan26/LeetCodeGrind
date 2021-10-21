class RandomizedSet:

    def __init__(self):
        self.vals = []
        self.locations = {}

    def insert(self, val: int) -> bool:
        if val not in self.locations:
            self.vals.append(val)
            self.locations[val] = len(self.vals) - 1
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.locations:
            loc = self.locations[val]
            last = self.vals[-1]
            self.vals[loc] = last
            self.locations[last] = loc
            self.vals.pop()
            self.locations.pop(val, 0)
            return True
        else:
            return False

    def getRandom(self) -> int:
        rand_val = random.randint(0, len(self.vals) - 1)
        return self.vals[rand_val]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()