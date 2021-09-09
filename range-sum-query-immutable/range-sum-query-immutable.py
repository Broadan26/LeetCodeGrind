class NumArray:

    def __init__(self, nums: list[int]):
        self.the_sums = []
        self.calculateSums(nums)

    def calculateSums(self, nums: list[int]):
        for i, num in enumerate(nums):
            if i == 0:
                self.the_sums.append(num)
            else:
                self.the_sums.append(self.the_sums[i-1] + num)

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.the_sums[right]
        return self.the_sums[right] - self.the_sums[left-1]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
