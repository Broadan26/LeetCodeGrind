class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        remove = 0
        if not intervals:
            return remove
        o_end = float('-inf')
        for start, end in sorted(intervals, key=lambda x: x[1]):
            if start >= o_end:
                o_end = end
            else:
                remove += 1
        return remove