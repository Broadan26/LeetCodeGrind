class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        answer = []
        i = 0
        while i < len(intervals) and intervals[i][0] < newInterval[0]: #Insert intervals before new one
            answer.append(intervals[i])
            i += 1

        if not answer or newInterval[0] > answer[-1][1]: # answer is empty or new interval doesn't overlap
            answer.append(newInterval)
        elif newInterval[1] > answer[-1][1]: # Last interval added overlaps with new interval
            answer[-1][1] = newInterval[1]

        for j in range(i, len(intervals)): # Insert remaining intervals
            if intervals[j][0] > answer[-1][1]: # No overlap, just insert
                answer.append(intervals[j])
            elif intervals[j][1] > answer[-1][1]: # Overlap occurs, merge
                answer[-1][1] = intervals[j][1]
        return answer