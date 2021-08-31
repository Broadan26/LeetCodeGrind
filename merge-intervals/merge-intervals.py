class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
        Given a list of a list of intervals
        Sorts the intervals by start and creates a merged interval list
        Returns the merged interval list as a list of intervals
        '''
        answer = []
        intervals.sort(key = lambda x: x[0]) #Sort each interval on its first element
        for i in range(len(intervals)):
            if not answer: #The answer is currently empty so append the interval
                answer.append(intervals[i])
            elif answer[-1][1] < intervals[i][0]: #The last element of the previous interval does not overlap
                answer.append(intervals[i])
            else: #The last element of the previous interval does overlap with start, so take the max
                answer[-1][1] = max(answer[-1][1], intervals[i][1])
        return answer