class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current = 0
        height_max = 0
        for change in gain:
            current += change
            height_max = max(current, height_max)
        return height_max