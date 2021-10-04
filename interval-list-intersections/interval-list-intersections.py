class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        answer = []
        if not firstList:
            return answer
        if not secondList:
            return answer
        
        first = second = 0
        while first < len(firstList) and second < len(secondList):
            lo = max(firstList[first][0], secondList[second][0])
            hi = min(firstList[first][1], secondList[second][1])
            if lo <= hi:
                answer.append([lo, hi])
            if firstList[first][1] < secondList[second][1]:
                first += 1
            else:
                second += 1

        return answer