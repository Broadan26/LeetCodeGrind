class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        total = 0
        for p in range(0, len(timeSeries)-1, 1):
            if timeSeries[p+1] > timeSeries[p] + duration:
                total += duration
            else:
                total += timeSeries[p+1] - timeSeries[p]
        return total + duration